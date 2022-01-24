from django import forms
from .models import Book
import re
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['name', 'genre', 'photo', 'author', 'url_to_download']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'url_to_download': forms.TextInput(attrs={"class": "form-control"}),
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if re.match(r'\d', title):
    #         raise ValidationError('Название недолжно начинаться с цифры')
    #     return title
