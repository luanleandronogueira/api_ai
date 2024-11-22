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
def search_page(request, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    loader = WebBaseLoader('https://bomjardim.pe.leg.br/API_pontomobile/index.html')
    dados_extraidos = loader.load()
    documentos = ''
    for doc in dados_extraidos:
        documentos = documentos + doc.page_content

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assitente amigável chamado itAI e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
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

   

