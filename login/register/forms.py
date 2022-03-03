from django import forms

class CreateNewUser (forms.Form):
    username = forms.CharField(label="Nome de usuáio", max_length=100)
    password = forms.CharField(label="Senha", max_length=8)
    # is_checked = forms.CheckboxInput()


class Login (forms.Form):
    username = forms.CharField(label="Nome de usuáio", max_length=100)
    password = forms.CharField(label="Senha", max_length=8)