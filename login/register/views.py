from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewUser, Login
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(response):
    show_error = False
    error_log = ""

    if response.method == 'POST':
        form = CreateNewUser(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # is_checked = form.cleaned_data['is_checked']

            if User.objects.filter(username=username).count() >= 1:
                print(User.objects.filter(username=username, password=password).count())
                show_error = True
                error_log = "Usuario já existente"
            else:
                show_error = False
                users_list = User(username=username, password=password)
                users_list.save()

                return HttpResponseRedirect('/register/login')
    else:
        form = CreateNewUser()

    return render(response, 'register/signup.html', {
        'form': form,
        'show_error': show_error,
        'error_log': error_log,
    })

def password_check():
    pass

def login(response):
    if response.method == 'POST':
        form = Login(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try: 
                User.objects.get(username=username, password=password)

                return HttpResponseRedirect('/')
            except ValueError:
                return HttpResponse('<h2>ERROR</h2>')
    else:
        form = Login()

    return render(response, 'register/login.html', {
        'form': form
    })

def log_out(response):
    pass