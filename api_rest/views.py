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

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')

def index(request):
    return render(request, 'chat_bot/index.html')

# Qualquer pergunta pode ser feita
@api_view(['GET'])
def pergunta_aberta(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        resposta = chat.invoke(pergunta)
        return Response({'Resposta': resposta.content}, status=200)

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
    
 
# Rotas para API para as páginas legistalitas dos menus da transparência 

# Menu de Gestão        
@api_view(['GET'])
def gestao(request, pergunta):
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
    
# Menu de RH    
@api_view(['GET'])
def rh(request, pergunta):
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
    

# Menu de Planejamento   
@api_view(['GET'])
def planejamento(request, pergunta):
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

# Menu de Demais Atos   
@api_view(['GET'])
def demais_atos(request, pergunta):
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
   

