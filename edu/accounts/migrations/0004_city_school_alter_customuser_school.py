# Generated by Django 4.0.1 on 2022-01-31 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_role_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название города')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название школы')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='Город')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school', verbose_name='Школа'),
        ),
    ]