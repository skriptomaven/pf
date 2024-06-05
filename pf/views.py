from django.shortcuts import render


def home_view(request):
    '''
    This is the 1st page users will see.
    '''
    return render(request, 'pf/home.html', {})

def login_view(request):
    '''
    Users will use this view to login.
    '''
    return render(request, 'pf/login.html', {})

def signup_view(request):
    '''
    Users will use this view to sign-up.
    '''
    return render(request, 'pf/signup.html', {})
