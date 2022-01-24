from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название книги')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    genre = models.ManyToManyField('Genre', verbose_name='Жанры')
    download_amount = models.IntegerField(default=0, verbose_name='Количество скачиваний')
    author = models.ManyToManyField('Author', verbose_name='Автор')
    url_to_download = models.TextField(max_length=300, default=None, verbose_name='Ссылка на скачивание')

    def get_absolute_url(self):
        return reverse('home') # !!

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Жанр')

    def get_absolute_url(self):
        return reverse('genre_books', kwargs={"genre_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    surname = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, db_index=True, verbose_name='Отчество')

    def get_absolute_url(self):
        return reverse('author_books', kwargs={"author_id": self.pk})

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
