from django.shortcuts import render
from .forms import UsersForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    form = UsersForm()
    return render(request, 'users/home.html', {'form': form})