from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm

class AccountForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'retype password'}))

    class Meta:
        model= Account
        fields = ['username', 'email']
