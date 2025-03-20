from django import forms

class UsersForm(forms.Form):
    nome = forms.CharField()