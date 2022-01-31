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
            'name': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                    'u-input '
                                                    'u-input-rectangle '
                                                    'u-white', 'type': 'text',
                                           'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                         'u-input '
                                                         'u-input-rectangle '
                                                         'u-white', 'type': 'text',
                                                'placeholder': 'Введите вашу фамилию'}),
            'patronymic': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                          'u-input '
                                                          'u-input-rectangle '
                                                          'u-white', 'type': 'text',
                                                 'placeholder': 'Введите ваше отчество'}),
            'email': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                     'u-input '
                                                     'u-input-rectangle '
                                                     'u-white', 'type': 'text',
                                            'placeholder': 'Введите ваш e-mail'}),
            'phone_number': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                            'u-input '
                                                            'u-input-rectangle '
                                                            'u-white', 'type': 'text',
                                                   'placeholder': 'Введите ваш номер'}),
            'username': forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                        'u-input '
                                                        'u-input-rectangle '
                                                        'u-white', 'type': 'text',
                                               'placeholder': 'Введите ваш логин'}),
            'password': forms.PasswordInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                            'u-input '
                                                            'u-input-rectangle '
                                                            'u-white', 'type': 'text',
                                                   'placeholder': 'Введите ваш пароль'}),
            'school': forms.Select(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                      'u-input '
                                                      'u-input-rectangle '
                                                      'u-white', 'type': 'text',
                                             'placeholder': 'Введите вашу школу'}),
            'role': forms.Select(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                 'u-input '
                                                 'u-input-rectangle '
                                                 'u-white', 'type': 'text',
                                        'placeholder': 'Выберите роль'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
                                                                                     'u-input '
                                                                                     'u-input-rectangle '
                                                                                     'u-white', 'type': 'text',
                                                                            'placeholder': 'Введите ваш логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'u-border-1 u-border-grey-30              u-input '
                                                   'u-input-rectangle u-white',
                                          'type': "password",
                                          'placeholder': "Введите пароль"}))

    # class LoginForm(forms.ModelForm):
    #     class Meta:
    #         model = User
    #         fields = ['username', 'password']
    #
    #     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-1 u-border-grey-30 '
    #                                                                                      'u-input '
    #                                                                                      'u-input-rectangle '
    #                                                                                      'u-white', 'type': 'text',
    #                                                                             'placeholder': 'Введите ваш логин',
    #                                                                             'id': 'name-ab3c',
    #                                                                             'name': 'name'}))
    #     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-1 u-border-grey-30 \
    #             u-input '
    #                                                                                           'u-input-rectangle u-white',
    #                                                                                  'type': "password",
    #                                                                                  'placeholder': "Введите пароль",
    #                                                                                  'id': "password-ab3c",
    #                                                                                  'name': "password"}))
    #
    #     def __init__(self, *args, **kwargs):
    #         self.request = kwargs.pop('request', None)
    #         super(LoginForm, self).__init__(*args, **kwargs)

# class UserRegistrationForm(forms.ModelForm):
#     username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Подтверждение пароля',
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError('Пароли не совпадают ')
#         return cd['password2']
