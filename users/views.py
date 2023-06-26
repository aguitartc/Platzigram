from click import echo #ja no s'usa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

#models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#exception
from django.db.utils import IntegrityError

#Forms
from users.forms import SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
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

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile
    
    def get_success_url(self) -> str:
        """return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
    
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

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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