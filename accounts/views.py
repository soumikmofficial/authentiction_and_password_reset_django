from django.shortcuts import render, redirect
from .forms import AccountForm

def signup(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'accounts/signup.html', {'form': form})

def home(request): 
    return render(request, 'accounts/home.html')

