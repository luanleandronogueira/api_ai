from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('user/<str:nick>', views.get_by_nick, name='get_by_nick'),
    # path('ai/<str:pergunta>', views.ask_question, name='ask_question'),
    path('pergunta_aberta/<str:pergunta>', views.pergunta_aberta, name='pergunta_aberta'),
    path('pergunta_especifica/<str:pergunta>', views.pergunta_especifica, name='pergunta_especifica'),
    path('gestao/<str:pergunta>', views.gestao, name='gestao'),
    path('rh/<str:pergunta>', views.rh, name='rh'),
    path('planejamento/<str:pergunta>', views.planejamento, name='planejamento'),
    path('demais_atos/<str:pergunta>', views.demais_atos, name='demais_atos'),
]
