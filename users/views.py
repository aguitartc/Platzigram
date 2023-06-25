from click import echo #ja no s'usa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

#models
from django.contrib.auth.models import User
from posts.models import Post

#exception
from django.db.utils import IntegrityError

#Forms
from users.forms import ProfileForm, SignupForm

class UserDetailView(DetailView):
    """User detail view."""
    template_name = "users/detail.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

@login_required
def update_profile(request): 
    """Update a user's profile view."""
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
    
def login_view(request): 
    """login view"""
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            print('NO TROBA USER*' * 10)
            # return redirect('users:login')
            return render(request, 'users/login.html', 
                          {'error':'Invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request): 
    """logout a user."""
    logout(request)
    return render(request, 'users/login.html')

def signup(request):
    """signup"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form': form
            }
    )
    
    return render(request,'users/signup.html')