from django import forms

class CreateNewUser (forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)
    # is_checked = forms.CheckboxInput()


class Login (forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)