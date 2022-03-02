from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewUser, Login
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(response):
    if response.method == 'POST':
        form = CreateNewUser(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            users_list = User(username=username, password=password)
            users_list.save()
        
        return HttpResponseRedirect('/login')
    else:
        form = CreateNewUser()

    return render(response, 'register/signup.html', {
        'form': form
    })

def login(response):
    if response.method == 'POST':
        form = Login(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #users_list = User()

            try: 
                User.objects.get(username=username, password=password)

                return HttpResponseRedirect('/')
            except:
                return HttpResponse('<h2>ERROR</h2>')
    else:
        form = Login()

    return render(response, 'register/login.html', {
        'form': form
    })