from django.db import models

# When adding models run command: python manage.py makemigration
# Then migrate

# Create your models here.
class ToDoList (models.Model):
    name = models.CharField(max_length=200) # Create an atribute, being a char[200]

    # Used to get the name when asking for the id, good for debugging
    # i.e. ToDoList.objects.get(id=id) -> <ToDoList: NameUSet>
    def __str__(self): 
        return self.name

class Item (models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # Create a foreing key cause ToDoList is an object not a field
    text = models.CharField(max_length=300)
    is_complete = models.BooleanField() # Create an boolean atribute

    def __str__(self):
        return self.text

class User (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Each item added to the database have an increasing id, starting from 1
# i.e. if we have 1 item, the id will be 1, 2 items id 2...