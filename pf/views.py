from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    '''
    This is the 1st page users will see.
    '''
    return render(request, 'pf/home.html', {})

def login(request):
    '''
    Users will use this view to login.
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect username or password!')
            return redirect('login')
    else:
        return render(request, 'pf/login.html', {})

def signup(request):
    '''
    Users will use this view to sign-up.
    '''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already exists!')
                return redirect(signup)
            elif User.objects.filter(email=email).exists():
                messages,info(request, 'Email already exists!')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                return redirect('login')
        else:
            messages.info(request, 'Password confirmation failed!')
            return redirect(signup)
    else:
        return render(request, 'pf/signup.html', {})

def logout(request):
    '''
    Logs out user.
    '''
    auth.logout(request)
    return redirect('home')
