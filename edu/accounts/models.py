from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название роли')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['name']


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name = 'Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Мобильный телефон')
    school = models.CharField(max_length=100, verbose_name='Школа')
    role = models.ForeignKey('Role', verbose_name='Роль пользователя', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
