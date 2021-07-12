from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('excluir_venda/<id_sticker>', views.excluir_venda, name='excluir_venda'),
]
