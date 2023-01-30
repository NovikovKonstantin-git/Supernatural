from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.home_page_one, name='home_page_one'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('articles/<int:articles_id>', view_articles, name='view_articles'),
    path('photo_gallery/', views.photo_gallery, name='photo_gallery'),
]
