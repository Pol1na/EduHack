# Generated by Django 4.0.1 on 2022-01-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='Имя'),
        ),
    ]
