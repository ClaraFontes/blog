from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set(request):
    request.session['names'] = {'nome1':'ana', 'nome2':'clara', 'nome3':'fontes'}
    request.session['idade'] = '20'
    # request.session.set_expiry(5)
    return HttpResponse('<h1> SET VIEW </h1>')

def get(request):
    nome = request.session['names']
    print(nome)
    print(request.session['idade'])
    # request.session['name'] = 'ana' # atualiza o dado 'name' para 'ana'
    print("a sessão expira em",request.session.get_expiry_age(), "segundos")
    return HttpResponse(f'<h1> GET VIEW - {nome} </h1>')

def delete(request):
    # del request.session['idade']
    request.session.flush() # deleta a session_key 
    request.session.clear_expired()
    return HttpResponse('<h1> DELETE VIEW </h1>')

def update(request):
    request.session['names']['nome1'] = 'Aninha'
    request.session.modified = True
    return HttpResponse("Update Page")