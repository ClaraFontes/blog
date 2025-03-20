from django.shortcuts import render
from .forms import UsersForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nome'])
            # lógica
            return HttpResponseRedirect('/users/obrigado/')
    else:
        form = UsersForm()
    return render(request, 'users/home.html', {'form': form})

def obrigado(request):
    return HttpResponse("FORMS ENVIADO!!")