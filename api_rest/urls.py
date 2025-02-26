from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Perguntas Abertas
    path('pergunta_aberta/<str:pergunta>', views.pergunta_aberta, name='pergunta_aberta'),
    path('pergunta_especifica/<str:pergunta>', views.pergunta_especifica, name='pergunta_especifica'),
    path('identifica_sentido/<str:pergunta>', views.identifica_sentido, name='identifica_sentido'),
    
    # ======================================== ENDPOINTS LEGISLATIVOS ================================================
    path('menu_completo_api_id/menu_completo/<int:id>/<str:pergunta>', views.menu_completo_api_id, name='menu_completo_api_id'),
    path('menu_completo/menu_completo/<int:id>/<str:pergunta>', views.menu_completo, name='menu_completo'),
    path('menu_completo/menu_completo_api_id_pref/<int:sigla>/<int:id>/<str:pergunta>', views.menu_completo_api_id_pref, name='menu_completo_pref'),
    path('gestao_api_id/gestao/<int:id>/<str:pergunta>', views.gestao_api_id, name='gestao_api_id'),
    path('receitas_despesas_api_id/receitas_despesas/<int:id>/<str:pergunta>', views.receitas_despesas_api_id, name='receitas_despesas_api_id'),
    path('planejamento_api_id/planejamento/<int:id>/<str:pergunta>', views.planejamento_api_id, name='planejamento_api_id'),
    path('relatorios_api_id/relatorios/<int:id>/<str:pergunta>', views.relatorios_api_id, name='relatorios_api_id'),
    path('rh_api_id/rh/<int:id>/<str:pergunta>', views.rh_api_id, name='rh_api_id'),
    path('demais_atos_api_id/demais_atos/<int:id>/<str:pergunta>', views.demais_atos_api_id, name='demais_atos_api_id'),
    path('legislativo_api_id/legislativo/<int:id>/<str:pergunta>', views.legislativo_api_id, name='legislativo_api_id'),
    # ======================================== FIM ENDPOINTS LEGISLATIVOS ================================================
    
    
  
    
]
