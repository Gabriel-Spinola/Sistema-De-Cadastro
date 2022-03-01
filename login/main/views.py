from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=id)

    return HttpResponse('<h1>%s</h1><h2>%s</h2>' % (ls.name, str(item.text)))

# Each item added to the database have an increasing id, starting from 1
# i.e. if we have 1 item, the id will be 1, 2 items id 2...