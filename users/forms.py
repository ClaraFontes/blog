from django import forms

class UsersForm(forms.Form):
    nome = forms.CharField(min_length=5, label="Seu Nome", label_suffix="", error_messages={'required': "Seu nome não pode estar vazio!", 'min_length':"O tamanho mínmo para este campo é de 5 caracteres."})
    email = forms.EmailField(required=False, label="Seu Email", label_suffix="", help_text="Apenas emails do Gmail são aceitos.")
    telefone = forms.IntegerField(label="Número para Contato", label_suffix="")