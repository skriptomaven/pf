from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone


from .forms import VideoForm
from .models import FlixUser, Video


def home(request):
    '''
    This is the 1st page users will see.
    '''
    videos = Video.objects.all()
    return render(request, 'pf/home.html', {'videos': videos})

def login(request):
    '''
    Logs registered users in.
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
            return redirect('signup')
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
            if FlixUser.objects.filter(username=username).exists():
                messages.info(request, 'User already exists!')
                return redirect(signup)
            elif FlixUser.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect(signup)
            else:
                user = FlixUser.objects.create_user(username=username, password=password, email=email)
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
    return redirect(home)

@login_required
def upload_video(request):
    '''
    Uploads video.
    '''
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return redirect(home)
    else:
        form = VideoForm
    return render(request, 'pf/video.html', {'form': form})
