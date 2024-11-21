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



@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    


@api_view(['GET'])
def ask_question(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        resposta = chat.invoke(pergunta)
        return Response({'Resposta': resposta.content}, status=200)


@api_view(['GET'])
def ask_question_template(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        template = ChatPromptTemplate.from_messages(
            [ ('system', 'Você é um especialista em geografia e história, responda sempre de forma simples porém com informações importantes'),
              ('user', 'Fale sobre a cidade {pergunta}')]
        )
        chain = template | chat
        
        resposta = chain.invoke(pergunta)
        return Response({'Resposta': resposta.content}, status=200)
    
@api_view(['GET'])
def search_page(request):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    loader = WebBaseLoader('http://app.camarabrejao.pe.gov.br/transparenciaMunicipal/carregaPortalCM.aspx?ID=27&e=C')
    dados_extraidos = loader.load()
    doc_html = ''
    for doc in dados_extraidos:
        doc_html += doc.page_content
        
    template = ChatPromptTemplate.from_messages([
        ('system', 'Você é um especialista em pesquisa e procura de dados e sempre responde em português brasil de forma educada e amigável'),
        ('user', 'Onde vejo as licitações?')
    ])

    chain = template | chat
    resposta = chain.invoke({'documentos informados' : doc_html})
    return Response({'Resposta': resposta.content}, status=200)    

