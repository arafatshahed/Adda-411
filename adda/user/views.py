from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def home(request):
    #return HttpResponse('<h1>User Home</h1>')
    context = {
        'title' : 'Home'
    }
    return render(request, 'user/home.html', context)

def profile(request):
    #return HttpResponse('<h1>User Profile</h1>')
    context = {
        'title' : 'Profile'
    }
    return render(request, 'user/profile.html', context)

def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    form = UserCreationForm()
    return render(request, 'user/login.html', {'form': form})
 