from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    return render(response, 'main/list.html', {
        # Variables dictionary
        'ls': ls
    })

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            to_do_list = ToDoList(name=name)

            to_do_list.save()

        return HttpResponseRedirect("/%i" % to_do_list.id)
    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {
        'form': form
    })