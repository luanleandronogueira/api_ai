from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick, name='get_by_nick'),
    path('ai/<str:pergunta>', views.ask_question, name='ask_question'),
    path('template/<str:pergunta>', views.ask_question_template, name='ask_question_template'),
    path('search/', views.search_page, name='search_page'),
]
