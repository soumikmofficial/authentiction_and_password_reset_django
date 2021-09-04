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

    # if request.method == "POST":
    #     form = AccountForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f'Your account was created successfully')
    #         return redirect('https://www.google.com/')
    #     else:
    #         return render(request, 'accounts/signup.html', {'form': form})
    # else:
    #     form = AccountForm()
    #     return render(request, 'accounts/signup.html', {'form': form})

