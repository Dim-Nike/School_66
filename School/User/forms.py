from django import  forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django.contrib.auth.models import Group


# Регистрация

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Enter your login'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                              'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                     'placeholder': 'Enter your password'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                           'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                           'placeholder': 'Enter your last name'}))
    email = forms.CharField(label='Эл. адрес', widget=forms.EmailInput(attrs={'class': 'form-input',
                                                                           'placeholder': 'Enter your email'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',  'catClassUser')


# Авторизация

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Enter your first name'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                              'placeholder': 'Enter your first name'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                     'placeholder': 'Enter your first name'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'photo', 'catClassUser', 'email')
