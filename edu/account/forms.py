from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'u-border-1 u-border-grey-30 u-input '
                                                                 'u-input-rectangle '
                                                              'u-white'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'u-border-1 u-border-grey-30 u-input '
                                                                         'u-input-rectangle u-white'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают ')
        return cd['password2']
