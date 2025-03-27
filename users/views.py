from django.shortcuts import render
from .forms import UsersForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
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
    user = User.objects.get(id=id) # será a instancia no else
    # print(user)
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return HttpResponseRedirect('/users/all-data/')
    else:
        form = UsersForm(instance=user)
    return render(request, 'users/update.html', {'form':form})

def deletar(request,id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.delete()
    return HttpResponseRedirect('/users/home/')
