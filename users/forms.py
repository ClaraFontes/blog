from django import forms

class UsersForm(forms.Form):
    nome = forms.CharField(min_length=5, label="Seu Nome", label_suffix="", error_messages={'required': "Seu nome não pode estar vazio!", 'min_length':"O tamanho mínmo para este campo é de 5 caracteres."}, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    email = forms.EmailField(required=False, label="Seu Email", label_suffix="", help_text="Apenas emails do Gmail são aceitos.", widget=forms.EmailInput(attrs={'placeholder':'Insira seu melhor email', 'class':'form-control'}))
    
    telefone = forms.IntegerField(label="Número para Contato", label_suffix="", widget=forms.NumberInput(attrs={'class':'form-control'}))

    bio = forms.CharField(widget=forms.Textarea(attrs={'cols':20, 'placeholder':'Bio', 'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']

        if nome[0] != 'c' and nome[0] != 'C':
            raise forms.ValidationError("A primeira letra do nome deve ser 'C'.")
        if email[0] != 'c' and email[0] != 'C':
            raise forms.ValidationError("A primeira letra do email deve ser 'C'.")