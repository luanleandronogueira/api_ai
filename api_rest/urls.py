from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.get_users, name='get_all_users'),
    path('', views.chat_bot, name='chat_bot'),
    path('user/<str:nick>', views.get_by_nick, name='get_by_nick'),
    path('ai/<str:pergunta>', views.ask_question, name='ask_question'),
    path('template/<str:pergunta>', views.ask_question_template, name='ask_question_template'),
    path('search/<str:pergunta>', views.search_page, name='search_page'),
    path('gestao/<str:pergunta>', views.gestao, name='gestao'),
    path('rh/<str:pergunta>', views.rh, name='rh'),
    path('planejamento/<str:pergunta>', views.planejamento, name='planejamento'),
]
