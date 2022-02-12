from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'patronymic', 'email', 'username', 'phone_number', 'school', 'role')
        labels = {'name': 'Имя', 'last_name': 'Фамилия', 'patronymic': 'Отчество', 'email': 'E-mail',
                  'username': 'Логин', 'phone_number': 'Номер телефона', 'school': 'Школа', 'role': 'Роль'}
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Введите вашу фамилию'}),
            'patronymic': forms.TextInput(attrs={
                'placeholder': 'Введите ваше отчество'}),
            'email': forms.TextInput(attrs={
                'placeholder': 'Введите ваш e-mail'}),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Введите ваш номер'}),
            'username': forms.TextInput(attrs={
                'placeholder': 'Введите ваш логин'}),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Введите ваш пароль'}),
            'school': forms.Select(attrs={
                'placeholder': 'Введите вашу школу'}),
            'role': forms.Select(attrs={
                'id': "combo2",
                'class': 'combo-input',
                'placeholder': 'Выберите роль'}),

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'})


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': "password",
                'placeholder': "Введите пароль"}))
