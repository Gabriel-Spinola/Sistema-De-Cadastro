from django.db import models

# When adding models run command: python manage.py makemigration
# Then migrate

# Create your models here.
class ToDoList (models.Model):
    name = models.CharField(max_length=200) # Create an atribute, being a char[200]

    def __str__(self):
        return self.name

class Item (models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # Create a foreing key cause ToDoList is an object not a field
    text = models.CharField(max_length=300)
    is_complete = models.BooleanField() # Create an boolean atribute

    def __str__(self):
        return self.text
