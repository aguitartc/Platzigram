from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#models
from django.contrib.auth.models import User
from users.models import Profile

#exception
from django.db.utils import IntegrityError


def update_profile(request): 
    return render(request, 'users/update_profile.html')

def login_view(request): 
    """login view"""
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            print('NO TROBA USER*' * 10)
            # return redirect('login')
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
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            newUser = User.objects.create_user(username=username, password= passwd)
        except:
            return render(request, 'users/signup.html', {'error': 'Username specified already exists'})
        
        newUser.first_name = request.POST['first_name']
        newUser.last_name = request.POST['last_name']
        newUser.save()

        profile = Profile(user=newUser)
        profile.save()

        return redirect('login')
    
    return render(request,'users/signup.html')