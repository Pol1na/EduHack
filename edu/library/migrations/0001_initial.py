# Generated by Django 4.0.1 on 2022-01-31 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(db_index=True, max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(db_index=True, max_length=50, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название книги')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('download_amount', models.IntegerField(default=0, verbose_name='Количество скачиваний')),
                ('url_to_download', models.TextField(default=None, max_length=300, verbose_name='Ссылка на скачивание')),
                ('author', models.ManyToManyField(to='library.Author', verbose_name='Автор')),
                ('genre', models.ManyToManyField(to='library.Genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name'],
            },
        ),
    ]
