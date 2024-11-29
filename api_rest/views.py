from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
from .models import User
from .serializes import UserSerializer
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
import json

# Chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview') # modelo do LLama que está sendo usando

def index(request):
    return render(request, 'chat_bot/index.html')

# Pergunta especifica sobre algum assunto relacionado ao tópico da pergunta
@api_view(['GET'])
def pergunta_especifica(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        template = ChatPromptTemplate.from_messages(
            [ ('system', 'Seu nome é ItAI. Você é um especialista em gestão pública, com foco em transparência, finanças públicas, e legislação municipal. Responda às perguntas com clareza e objetividade, utilizando uma linguagem simples para facilitar o entendimento de pessoas com conhecimento básico no tema. Forneça informações importantes, contextualize com exemplos práticos quando possível, e inclua dados ou referências relevantes para fortalecer a resposta.'),
              ('user', ' {pergunta}')]
        )
        chain = template | chat
        
        resposta = chain.invoke(pergunta)
        return Response({'Resposta': resposta.content}, status=200)
    
# Qualquer pergunta pode ser feita
@api_view(['GET'])
def pergunta_aberta(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        resposta = chat.invoke(pergunta)
        return Response({'Resposta': resposta.content}, status=200)
 



# Rotas para API para as páginas legistalitas dos menus da transparência 

# ----------------------------- Endpoint CM Garanhuns ---------------------------------#

# Menu de Gestão Garanhuns       
@api_view(['GET'])
def gestao_cm_garanhuns(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Garanhuns  
@api_view(['GET'])
def rh_cm_garanhuns(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento Garanhuns   
@api_view(['GET'])
def planejamento_cm_garanhuns(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
       
# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_garanhuns(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Garanhuns 
@api_view(['GET'])
def demais_atos_cm_garanhuns(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Garanhuns ---------------------------------#

# ----------------------------- Endpoint CM Angelim ---------------------------------#

# Menu de Gestão angelim       
@api_view(['GET'])
def gestao_cm_angelim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH angelim  
@api_view(['GET'])
def rh_cm_angelim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Planejamento angelim   
@api_view(['GET'])
def planejamento_cm_angelim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_angelim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Demais Atos angelim 
@api_view(['GET'])
def demais_atos_cm_angelim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM angelim ---------------------------------#

# ----------------------------- Endpoint CM Bom Conselho ---------------------------------#

# Menu de Gestão bom_conselho       
@api_view(['GET'])
def gestao_cm_bom_conselho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH bom_conselho  
@api_view(['GET'])
def rh_cm_bom_conselho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento bom_conselho   
@api_view(['GET'])
def planejamento_cm_bom_conselho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_bom_conselho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Demais Atos bom_conselho 
@api_view(['GET'])
def demais_atos_cm_bom_conselho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Bom Conselho ---------------------------------#

# ----------------------------- Endpoint CM Canhotinho ---------------------------------#

# Menu de Gestão canhotinho       
@api_view(['GET'])
def gestao_cm_canhotinho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH canhotinho  
@api_view(['GET'])
def rh_cm_canhotinho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento canhotinho   
@api_view(['GET'])
def planejamento_cm_canhotinho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_canhotinho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Demais Atos canhotinho 
@api_view(['GET'])
def demais_atos_cm_canhotinho(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Canhotinho ---------------------------------#

# ----------------------------- Endpoint CM Correntes ---------------------------------#

# Menu de Gestão correntes       
@api_view(['GET'])
def gestao_cm_correntes(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH correntes  
@api_view(['GET'])
def rh_cm_correntes(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_correntes(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento correntes   
@api_view(['GET'])
def planejamento_cm_correntes(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos correntes 
@api_view(['GET'])
def demais_atos_cm_correntes(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Correntes ---------------------------------#

# ----------------------------- Endpoint CM Ingazeira ---------------------------------#

# Menu de Gestão ingazeira       
@api_view(['GET'])
def gestao_cm_ingazeira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH ingazeira  
@api_view(['GET'])
def rh_cm_ingazeira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento ingazeira   
@api_view(['GET'])
def planejamento_cm_ingazeira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_ingazeira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos ingazeira 
@api_view(['GET'])
def demais_atos_cm_ingazeira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Ingazeira ---------------------------------#

# ----------------------------- Endpoint CM Jaqueira ---------------------------------#
  
# Menu de Gestão jaqueira       
@api_view(['GET'])
def gestao_cm_jaqueira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH jaqueira  
@api_view(['GET'])
def rh_cm_jaqueira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento jaqueira   
@api_view(['GET'])
def planejamento_cm_jaqueira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_jaqueira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos jaqueira 
@api_view(['GET'])
def demais_atos_cm_jaqueira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Jaqueira ---------------------------------#

# ----------------------------- Endpoint CM Tabira ---------------------------------#
  
# Menu de Gestão tabira       
@api_view(['GET'])
def gestao_cm_tabira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH tabira  
@api_view(['GET'])
def rh_cm_tabira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento tabira   
@api_view(['GET'])
def planejamento_cm_tabira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_tabira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos tabira 
@api_view(['GET'])
def demais_atos_cm_tabira(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Tabira ---------------------------------#

# ----------------------------- Endpoint CM Brejão ---------------------------------#
  
# Menu de Gestão Brejão       
@api_view(['GET'])
def gestao_cm_brejao(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Brejão  
@api_view(['GET'])
def rh_cm_brejao(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Planejamento Brejão   
@api_view(['GET'])
def planejamento_cm_brejao(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_brejao(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Brejão 
@api_view(['GET'])
def demais_atos_cm_brejao(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Brejão ---------------------------------#

# ----------------------------- Endpoint CM Iguaracy ---------------------------------#
  
# Menu de Gestão Iguaracy       
@api_view(['GET'])
def gestao_cm_iguaracy(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Iguaracy  
@api_view(['GET'])
def rh_cm_iguaracy(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento Iguaracy   
@api_view(['GET'])
def planejamento_cm_iguaracy(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_iguaracy(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Iguaracy 
@api_view(['GET'])
def demais_atos_cm_iguaracy(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Iguaracy ---------------------------------#

# ----------------------------- Endpoint CM Jucati ---------------------------------#
  
# Menu de Gestão Jucati       
@api_view(['GET'])
def gestao_cm_jucati(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Jucati  
@api_view(['GET'])
def rh_cm_jucati(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Planejamento Jucati   
@api_view(['GET'])
def planejamento_cm_jucati(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_jucati(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Jucati 
@api_view(['GET'])
def demais_atos_cm_jucati(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Jucati ---------------------------------#

# ----------------------------- Endpoint CM Quipapá ---------------------------------#
  
# Menu de Gestão Quipapá       
@api_view(['GET'])
def gestao_cm_quipapa(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Quipapá  
@api_view(['GET'])
def rh_cm_quipapa(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento Quipapá   
@api_view(['GET'])
def planejamento_cm_quipapa(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_quipapa(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Quipapá 
@api_view(['GET'])
def demais_atos_cm_quipapa(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Quipapá ---------------------------------#

# ----------------------------- Endpoint CM Bom Jardim ---------------------------------#
  
# Menu de Gestão Bom Jardim       
@api_view(['GET'])
def gestao_cm_bom_jardim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH bom_jardim  
@api_view(['GET'])
def rh_cm_bom_jardim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento bom_jardim   
@api_view(['GET'])
def planejamento_cm_bom_jardim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_bom_jardim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Bom Jardim 
@api_view(['GET'])
def demais_atos_cm_bom_jardim(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Bom Jardim ---------------------------------#

# ----------------------------- Endpoint CM Tuparetama ---------------------------------#
  
# Menu de Gestão Tuparetama       
@api_view(['GET'])
def gestao_cm_tuparetama(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/gestao.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de RH Tuparetama  
@api_view(['GET'])
def rh_cm_tuparetama(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/rh.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu de Planejamento Tuparetama   
@api_view(['GET'])
def planejamento_cm_tuparetama(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Relatorios  
@api_view(['GET'])
def relatorios_cm_tuparetama(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/relatorios.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu de Demais Atos Tuparetama 
@api_view(['GET'])
def demais_atos_cm_tuparetama(request, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/api/planejamento.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat
    # resposta = chain.invoke({'documentos_informados' : documentos, 'input' : pergunta})
    documentos = documentos[:4000]
    try:
        resposta = chain.invoke({'documentos_informados': documentos, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# ----------------------------- Fim Endpoint CM Tuparetama ---------------------------------#



# Exemplo de API de consulta
# @api_view(['GET'])
# def get_users(request):
    
#     if request.method == 'GET':
#         users = User.objects.all()
        
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    
#     return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_by_nick(request, nick):
#     try:
#         user = User.objects.get(pk=nick)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
   

