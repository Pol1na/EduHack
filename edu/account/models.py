from django.db import models
from django.contrib import auth


class User(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=64)
    office_number = models.CharField(max_length=64)