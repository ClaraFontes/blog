from django.shortcuts import render
from .forms import UsersForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            bio = form.cleaned_data['bio']

            user = User.objects.create(nome=nome, email=email, telefone=telefone, bio=bio)

            return HttpResponseRedirect('/users/obrigado/')
    else:
        form = UsersForm()
    return render(request, 'users/home.html', {'form': form})

def obrigado(request):
    return HttpResponse("FORMS ENVIADO!!")