from django.urls import path

from .views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    # path('register_done/', register, name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    path('login/', user_login, name='login'),
    # path('test/', test, name='test'),
    # path('register/', index, name='register'),
    # path('library/search/', SearchResultBookView.as_view(), name='search'),
    # path('library/add_book/', CreateBook.as_view(), name='add_book'),
    # path('register/', register, name="register"),
    # path('login/', login, name="login"),
    # path('cat/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # # path('news/add-news/', add_news, name='add_news'),
    # path('news/add-news/', CreateNews.as_view(), name='add_news'),

]
