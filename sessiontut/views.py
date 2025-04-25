from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set(request):
    request.session['name'] = 'clara'
    request.session['idade'] = '20'
    request.session.set_expiry(5)
    return HttpResponse('<h1> SET VIEW </h1>')

def get(request):
    print(request.session['name'])
    print(request.session['idade'])
    # request.session['name'] = 'ana' # atualiza o dado 'name' para 'ana'
    print("a sessão expira em",request.session.get_expiry_age(), "segundos")
    return HttpResponse('<h1> GET VIEW </h1>')

def delete(request):
    # del request.session['idade']
    request.session.flush() # deleta a session_key 
    request.session.clear_expired()
    return HttpResponse('<h1> DELETE VIEW </h1>')