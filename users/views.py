from django.shortcuts import render
from .forms import UsersForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        form = UsersForm()
    form = UsersForm()
    return render(request, 'users/home.html', {'form': form})