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


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название школы')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
        ordering = ['name']


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, default=1, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone_number = models.CharField(max_length=11, verbose_name='Мобильный телефон')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    role = models.ForeignKey('Role', verbose_name='Роль пользователя', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
