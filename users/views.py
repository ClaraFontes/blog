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

def dados(request):
    alldata = User.objects.all()
    return render(request, 'users/alldata.html', {'all_data':alldata})

def atualizar(request,id):
    user = User.objects.get(id=id)
    # print(user)
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            user.nome = form.cleaned_data['nome']
            user.email = form.cleaned_data['email']
            user.telefone = form.cleaned_data['telefone']
            user.bio = form.cleaned_data['bio']
            user.save()
    else:
        form = UsersForm(initial={'nome':user.nome,'email':user.email,'telefone':user.telefone,'bio':user.bio})
    return render(request, 'users/update.html', {'form':form})

def deletar(request,id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.delete()
    return HttpResponseRedirect('/users/home/')