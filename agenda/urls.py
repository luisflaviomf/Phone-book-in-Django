from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', contatos, name='index'),
    path('contatocriar', contatocriar, name='contatocriar'),
    path('contatoupdate/<int:id>/', contatoupdate, name='contatoupdate'),
    path('contatodelete/<int:id>/', contatodelete, name='contatodelete'),
]
