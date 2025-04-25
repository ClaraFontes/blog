from django.shortcuts import render
from .forms import UsersForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
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

def set(request):
    print("view 'set' foi chamada")
    response = HttpResponse("Setting cookiess")
    response.set_cookie('tema','dark')
    response.set_cookie('nome', 'clara', max_age=5)
    response.set_cookie('teste', '123')
    return response

def set_com_render(request):
    response = render(request, "users/home.html")
    response.set_cookie('tema','light')
    return response

def set_com_TemplateResponse(request):
    print("view 'set_com_TemplateResponse' foi chamada")
    response = TemplateResponse(request, "users/home.html",{'name':'clarota'})
    response.set_cookie('usuario','me myself and I')
    return response

def get(request):
    # raise Exception("Exceção da view 'get'")
    tema = request.COOKIES['tema']
    return HttpResponse(f'atual tema da pagina: {tema}')

def delete(request):
    response = HttpResponse('deletado')
    response.delete_cookie('tema')
    response.delete_cookie('teste')
    response.delete_cookie('usuario')
    return response

def update(request):
    response = HttpResponse('atualizado')
    response.set_cookie('nome','Ana')
    return response
