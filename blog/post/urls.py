from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from .views import *



urlpatterns = [

    path('', home, name='home'),
    path('index/', post_index, name='index'),
    path('<int:id>', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('category/<int:id>', blogs_by_category, name='blogs_by_category'),
    path('update/', post_update, name='update'),
    path('delete/', post_delete, name='delete')

]
