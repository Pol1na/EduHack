from django.urls import path

from .views import *

urlpatterns = [
    path('profile/<int:pk>', profile, name='profile'),
]
