from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic import UpdateView

# Create your views here.
def register(response):
    if response.method == "POST":
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password']
        password2 = response.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(response, "This email already exists in our database")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.error(response, "This username already exists in our database")
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                new_user = auth.authenticate(username=username, password=password)
                auth.login(response, new_user)
                return redirect('index')

        else:
            messages.error(response, "The passwords do not match")
            return redirect('register')

    return render(response, ('registration/register.html'))

def login(response):
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(response, user)
            return redirect('index')

        else:
            messages.error(response, "Invalid credentials. Please try again")
    return render(response, ('registration/login.html'))

def logout(response):
    auth.logout(response)
    return redirect('index')