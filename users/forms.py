from django import forms
from django.core import validators
from .models import User

def start_with_c(valor):
    if valor[0] != 'c' and valor[0] != 'C':
        raise forms.ValidationError("Este campo deve começar com a letra C.")

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'telefone', 'bio']
        labels = {
            'nome':'Seu Nome',
            'email':'Seu Email',
            'telefone':'Número para contato',
            'bio':'Sobre Você'
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefone':forms.NumberInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'})
        }
        help_texts = {
            'email':'Só são aceitos Gmails'
        }
        error_messages = {
            'nome':{
                'required':'Este campo é obrigatório!'
            }
        }

    # nome = forms.CharField(validators=[validators.MaxLengthValidator(10), start_with_c],min_length=5, label="Seu Nome", label_suffix="", error_messages={'required': "Seu nome não pode estar vazio!", 'min_length':"O tamanho mínmo para este campo é de 5 caracteres."}, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    # email = forms.EmailField(required=False, label="Seu Email", label_suffix="", help_text="Apenas emails do Gmail são aceitos.", widget=forms.EmailInput(attrs={'placeholder':'Insira seu melhor email', 'class':'form-control'}), validators=[start_with_c])
    
    # telefone = forms.IntegerField(label="Número para Contato", label_suffix="", widget=forms.NumberInput(attrs={'class':'form-control'}))

    # bio = forms.CharField(widget=forms.Textarea(attrs={'cols':20, 'placeholder':'Bio', 'class':'form-control'}))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     nome = self.cleaned_data['nome']
    #     email = self.cleaned_data['email']

    #     if nome[0] != 'c' and nome[0] != 'C':
    #         raise forms.ValidationError("A primeira letra do nome deve ser 'C'.")
    #     if email[0] != 'c' and email[0] != 'C':
    #         raise forms.ValidationError("A primeira letra do email deve ser 'C'.")