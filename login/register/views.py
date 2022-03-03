from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewUser, Login
from .models import User

# Create your views here.
def sign_up(response):
    show_error = False
    error_log = ""

    if response.method == 'POST':
        form = CreateNewUser(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #is_checked = form.cleaned_data['is_checked']

            if User.objects.filter(username=username).count() >= 1:
                show_error = True
                error_log = "Usuario já existente"
            else:
                is_password_valid, error = password_check(password)

                if not is_password_valid:
                    show_error = True
                    error_log = error
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

def password_check(passwd): 
    if len(passwd) < 4:
        return False, 'A senha tem que ter pelo menos 4 caracteres'
    if len(passwd) > 20:
        return False, 'A senha não pode ser maior do que 4 caracteres'
    if not any(char.isdigit() for char in passwd):
        return False, 'Password should have at least one numeral'
    if not any(char.isupper() for char in passwd):
        return False, 'Password should have at least one uppercase letter'
    if not any(char.islower() for char in passwd):
        return False, 'Password should have at least one lowercase letter'

    return True, ''

def login(response):
    if response.session.get('is_logged_in') is None:
        response.session['is_logged_in'] = False

    show_error = False
    error_log = ""

    if response.method == 'POST':
        form = Login(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try: 
                User.objects.get(username__exact=username, password__exact=password)

                response.session['is_logged_in'] = True

                return HttpResponseRedirect('/')
            except:
                show_error = True
                error_log = "Usuario ou senha incorretos"
    else:
        form = Login()

    return render(response, 'register/login.html', {
        'form': form,
        'show_error': show_error,
        'error_log': error_log,
    })

def log_out(response):
    pass