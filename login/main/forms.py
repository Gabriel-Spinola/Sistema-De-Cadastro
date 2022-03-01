from django import forms

# For every form you create you'll need a new class

class CreateNewList (forms.Form):
    name = forms.CharField(label="Name", max_length=200) # Same as adding attributes to the database
    check = forms.BooleanField(required=False)