from aiohttp import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList

def manage_session(response) -> bool:
    if response.session.get('is_logged_in') == None:
        response.session['is_logged_in'] = False

        return True
    elif response.session.get('is_logged_in') == False:
        return True

    return False

# Create your views here.
def index(response, id):
    if manage_session(response):
        return HttpResponseRedirect('/register/login')

    ls = ToDoList.objects.get(id=id)

    if response.method == 'POST':
        print(response.POST)

        # Get POST request and ask for a specific information, 
        # in this situation the button named 'save'
        if response.POST.get('save'): 
            for item in ls.item_set.all():
                # Check if we completed an item
                item.is_complete = response.POST.get('c' + str(item.id)) == 'clicked'

                item.save()
        elif response.POST.get('newItem'):
            txt = response.POST.get('new') # Get the input field text
            
            # Cause We're using a custom form we don't have the is_valid function
            if len(txt) > 2:
                ls.item_set.create(text=txt, is_complete=False)
            else:
                print('INVALID INPUT')

    return render(response, 'main/list.html', {
        # Variables dictionary
        'ls': ls,
    })

def home(response):
    if manage_session(response):
        return HttpResponseRedirect('/register/login')

    return render(response, 'main/home.html', {})

def create(response):
    if manage_session(response):
        return HttpResponseRedirect('/register/login')

    # Receive Post method
    if response.method == 'POST': 
        form = CreateNewList(response.POST)

        # if there's no error in the form
        if form.is_valid(): 
            name = form.cleaned_data['name']

            # Create and save a new to do list with the form data
            to_do_list = ToDoList(name=name)
            to_do_list.save()

        # Redirect to the new to do list's page
        return HttpResponseRedirect("/%i" % to_do_list.id)
    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {
        'form': form
    })

def logout(response):
    del response.session['is_logged_in']

    return HttpResponseRedirect('/register/login')

    