from django import forms

# For every form you create you'll need a new class

class CreateNewList (forms.Form):
    name = forms.CharField(label="Name", max_length=200) # Same as adding attributes to the database
    check = forms.BooleanField(required=False)

class CreateNewUser (forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)