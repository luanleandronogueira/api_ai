from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Perguntas Abertas
    path('pergunta_aberta/<str:pergunta>', views.pergunta_aberta, name='pergunta_aberta'),
    path('pergunta_especifica/<str:pergunta>', views.pergunta_especifica, name='pergunta_especifica'),
    
    
    # ======================================== ENDPOINTS LEGISLATIVOS ================================================
    
    # Endpoints Câmara Garanhuns
    path('cm_garanhuns/gestao/<str:pergunta>', views.gestao_cm_garanhuns, name='gestao_cm_garanhuns'),
    path('cm_garanhuns/rh/<str:pergunta>', views.rh_cm_garanhuns, name='rh_cm_garanhuns'),
    path('cm_garanhuns/planejamento/<str:pergunta>', views.planejamento_cm_garanhuns, name='planejamento_cm_garanhuns'),
    path('cm_garanhuns/relatorios/<str:pergunta>', views.relatorios_cm_garanhuns, name='relatorios_cm_garanhuns'),
    path('cm_garanhuns/demais_atos/<str:pergunta>', views.demais_atos_cm_garanhuns, name='demais_atos_cm_garanhuns'),
    
    # Endpoints Câmara Angelim
    path('cm_angelim/gestao/<str:pergunta>', views.gestao_cm_angelim, name='gestao_cm_angelim'),
    path('cm_angelim/rh/<str:pergunta>', views.rh_cm_angelim, name='rh_cm_angelim'),
    path('cm_angelim/planejamento/<str:pergunta>', views.planejamento_cm_angelim, name='planejamento_cm_angelim'),
    path('cm_angelim/relatorios/<str:pergunta>', views.relatorios_cm_angelim, name='relatorios_cm_angelim'),
    path('cm_angelim/demais_atos/<str:pergunta>', views.demais_atos_cm_angelim, name='demais_atos_cm_angelim'),
    
    # Endpoints Câmara Bom Conselho
    path('cm_bom_conselho/gestao/<str:pergunta>', views.gestao_cm_bom_conselho, name='gestao_cm_bom_conselho'),
    path('cm_bom_conselho/rh/<str:pergunta>', views.rh_cm_bom_conselho, name='rh_cm_bom_conselho'),
    path('cm_bom_conselho/planejamento/<str:pergunta>', views.planejamento_cm_bom_conselho, name='planejamento_bom_conselho'),
    path('cm_bom_conselho/relatorios/<str:pergunta>', views.relatorios_cm_bom_conselho, name='relatorios_cm_bom_conselho'),
    path('cm_bom_conselho/demais_atos/<str:pergunta>', views.demais_atos_cm_bom_conselho, name='demais_atos_bom_conselho'),
    
    # Endpoints Câmara Canhotinho
    path('cm_canhotinho/gestao/<str:pergunta>', views.gestao_cm_canhotinho, name='gestao_cm_canhotinho'),
    path('cm_canhotinho/rh/<str:pergunta>', views.rh_cm_canhotinho, name='rh_cm_canhotinho'),
    path('cm_canhotinho/planejamento/<str:pergunta>', views.planejamento_cm_canhotinho, name='planejamento_cm_canhotinho'),
    path('cm_canhotinho/relatorios/<str:pergunta>', views.relatorios_cm_canhotinho, name='relatorios_cm_canhotinho'),
    path('cm_canhotinho/demais_atos/<str:pergunta>', views.demais_atos_cm_canhotinho, name='demais_atos_cm_canhotinho'),
    
    # Endpoints Câmara Correntes
    path('cm_correntes/gestao/<str:pergunta>', views.gestao_cm_correntes, name='gestao_cm_correntes'),
    path('cm_correntes/rh/<str:pergunta>', views.rh_cm_correntes, name='rh_cm_correntes'),
    path('cm_correntes/planejamento/<str:pergunta>', views.planejamento_cm_correntes, name='planejamento_cm_correntes'),
    path('cm_correntes/relatorios/<str:pergunta>', views.relatorios_cm_correntes, name='relatorios_cm_correntes'),
    path('cm_correntes/demais_atos/<str:pergunta>', views.demais_atos_cm_correntes, name='demais_atos_cm_correntes'),
    
    # Endpoints Câmara Ingazeira
    path('cm_ingazeira/gestao/<str:pergunta>', views.gestao_cm_ingazeira, name='gestao_cm_ingazeira'),
    path('cm_ingazeira/rh/<str:pergunta>', views.rh_cm_ingazeira, name='rh_cm_ingazeira'),
    path('cm_ingazeira/planejamento/<str:pergunta>', views.planejamento_cm_ingazeira, name='planejamento_cm_ingazeira'),
    path('cm_ingazeira/relatorios/<str:pergunta>', views.relatorios_cm_ingazeira, name='relatorios_cm_ingazeira'),
    path('cm_ingazeira/demais_atos/<str:pergunta>', views.demais_atos_cm_ingazeira, name='demais_atos_cm_ingazeira'),
    
    # Endpoints Câmara Jaqueira
    path('cm_jaqueira/gestao/<str:pergunta>', views.gestao_cm_jaqueira, name='gestao_cm_jaqueira'),
    path('cm_jaqueira/rh/<str:pergunta>', views.rh_cm_jaqueira, name='rh_cm_jaqueira'),
    path('cm_jaqueira/planejamento/<str:pergunta>', views.planejamento_cm_jaqueira, name='planejamento_cm_jaqueira'),
    path('cm_jaqueira/relatorios/<str:pergunta>', views.relatorios_cm_jaqueira, name='relatorios_cm_jaqueira'),
    path('cm_jaqueira/demais_atos/<str:pergunta>', views.demais_atos_cm_jaqueira, name='demais_atos_cm_jaqueira'),
    
    # Endpoints Câmara Tabira
    path('cm_tabira/gestao/<str:pergunta>', views.gestao_cm_tabira, name='gestao_cm_tabira'),
    path('cm_tabira/rh/<str:pergunta>', views.rh_cm_tabira, name='rh_cm_tabira'),
    path('cm_tabira/planejamento/<str:pergunta>', views.planejamento_cm_tabira, name='planejamento_cm_tabira'),
    path('cm_tabira/relatorios/<str:pergunta>', views.relatorios_cm_tabira, name='relatorios_cm_tabira'),
    path('cm_tabira/demais_atos/<str:pergunta>', views.demais_atos_cm_tabira, name='demais_atos_cm_tabira'),
    
    # Endpoints Câmara Brejão
    path('cm_brejao/gestao/<str:pergunta>', views.gestao_cm_brejao, name='gestao_cm_brejao'),
    path('cm_brejao/rh/<str:pergunta>', views.rh_cm_brejao, name='rh_cm_brejao'),
    path('cm_brejao/planejamento/<str:pergunta>', views.planejamento_cm_brejao, name='planejamento_cm_brejao'),
    path('cm_brejao/relatorios/<str:pergunta>', views.relatorios_cm_brejao, name='relatorios_cm_brejao'),
    path('cm_brejao/demais_atos/<str:pergunta>', views.demais_atos_cm_brejao, name='demais_atos_cm_brejao'),
    
    # Endpoints Câmara Iguaracy
    path('cm_iguaracy/gestao/<str:pergunta>', views.gestao_cm_iguaracy, name='gestao_cm_iguaracy'),
    path('cm_iguaracy/rh/<str:pergunta>', views.rh_cm_iguaracy, name='rh_cm_iguaracy'),
    path('cm_iguaracy/planejamento/<str:pergunta>', views.planejamento_cm_iguaracy, name='planejamento_cm_iguaracy'),
    path('cm_iguaracy/relatorios/<str:pergunta>', views.relatorios_cm_iguaracy, name='relatorios_cm_iguaracy'),
    path('cm_iguaracy/demais_atos/<str:pergunta>', views.demais_atos_cm_iguaracy, name='demais_atos_cm_iguaracy'),
    
    # Endpoints Câmara Jucati
    path('cm_jucati/gestao/<str:pergunta>', views.gestao_cm_jucati, name='gestao_cm_jucati'),
    path('cm_jucati/rh/<str:pergunta>', views.rh_cm_jucati, name='rh_cm_jucati'),
    path('cm_jucati/planejamento/<str:pergunta>', views.planejamento_cm_jucati, name='planejamento_cm_jucati'),
    path('cm_jucati/relatorios/<str:pergunta>', views.relatorios_cm_jucati, name='relatorios_cm_jucati'),
    path('cm_jucati/demais_atos/<str:pergunta>', views.demais_atos_cm_jucati, name='demais_atos_cm_jucati'),
    
    # Endpoints Câmara Quipapá
    path('cm_quipapa/gestao/<str:pergunta>', views.gestao_cm_quipapa, name='gestao_cm_quipapa'),
    path('cm_quipapa/rh/<str:pergunta>', views.rh_cm_quipapa, name='rh_cm_quipapa'),
    path('cm_quipapa/planejamento/<str:pergunta>', views.planejamento_cm_quipapa, name='planejamento_cm_quipapa'),
    path('cm_quipapa/relatorios/<str:pergunta>', views.relatorios_cm_quipapa, name='relatorios_cm_quipapa'),
    path('cm_quipapa/demais_atos/<str:pergunta>', views.demais_atos_cm_quipapa, name='demais_atos_cm_quipapa'),
    
    # Endpoints Câmara Bom Jardim
    path('cm_bom_jardim/gestao/<str:pergunta>', views.gestao_cm_bom_jardim, name='gestao_cm_bom_jardim'),
    path('cm_bom_jardim/rh/<str:pergunta>', views.rh_cm_bom_jardim, name='rh_cm_bom_jardim'),
    path('cm_bom_jardim/planejamento/<str:pergunta>', views.planejamento_cm_bom_jardim, name='planejamento_cm_bom_jardim'),
    path('cm_bom_jardim/relatorios/<str:pergunta>', views.relatorios_cm_bom_jardim, name='relatorios_cm_bom_jardim'),
    path('cm_bom_jardim/demais_atos/<str:pergunta>', views.demais_atos_cm_bom_jardim, name='demais_atos_cm_bom_jardim'),

    # Endpoints Câmara Tuparetama
    path('cm_tuparetama/gestao/<str:pergunta>', views.gestao_cm_tuparetama, name='gestao_cm_tuparetama'),
    path('cm_tuparetama/rh/<str:pergunta>', views.rh_cm_tuparetama, name='rh_cm_tuparetama'),
    path('cm_tuparetama/planejamento/<str:pergunta>', views.planejamento_cm_tuparetama, name='planejamento_cm_tuparetama'),
    path('cm_tuparetama/relatorios/<str:pergunta>', views.relatorios_cm_tuparetama, name='relatorios_cm_tuparetama'),
    path('cm_tuparetama/demais_atos/<str:pergunta>', views.demais_atos_cm_tuparetama, name='demais_atos_cm_tuparetama'),
    
    # ======================================== FIM ENDPOINTS LEGISLATIVOS ================================================
]
