# Generated by Django 4.0.1 on 2022-01-31 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_city_school_alter_customuser_school'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['name'], 'verbose_name': 'Школа', 'verbose_name_plural': 'Школы'},
        ),
    ]