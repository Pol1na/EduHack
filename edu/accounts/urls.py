from django.urls import path

from .views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', user_login, name='login'),

]
