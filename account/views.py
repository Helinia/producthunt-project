from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth




def signup(request):
    if request.method == 'POST':
        #user has info and wants an account.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html',{'error':'user has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html',{'error':'Password must match.'})
    else:
        #user wants to enter info
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html',{'error':'username or password is incorrect'})


    else:
        return render(request, 'account/login.html')


def logout(request):
    #Have to make sure that it is a POST request!
    #Since Google Chrome will actively pre-load the webpages.
    #If it is a GET request, it will automatically log out the user.

    #TODO: need to route to homepage and don't forget to logout.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
