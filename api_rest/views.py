from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
from .models import User
from .serializes import UserSerializer
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
import spacy
import json

# Chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview') # modelo do LLama que está sendo usando

# Temas que serão pesquisados
# Temas = {
#     "gestão": "temp/gestao.html",
#     "finanças": "temp/gestao.html",
#     "audiência pública": "temp/gestao.html",
#     "carta de serviços": "temp/gestao.html",
#     "estrutura organizacional": "temp/gestao.html",
#     "dados abertos": "temp/demais_atos.html",
#     "informações sigilosas": "temp/gestao.html",
#     "editais e concursos": "temp/gestao.html",
#     "consulta do duodécimo": "temp/receitas_despesas.html",
#     "receitas extraorçamentárias": "temp/receitas_despesas.html",
#     "despesas consolidadas": "temp/receitas_despesas.html",
#     "despesas detalhadas": "temp/receitas_despesas.html",
#     "orçamento público": "temp/receitas_despesas.html",
#     "controle interno": "temp/receitas_despesas.html",
#     "transparência": "temp/receitas_despesas.html",
#     "planejamento estratégico": "temp/gestao.html",
#     "responsabilidade fiscal": "temp/receitas_despesas.html",
#     "políticas públicas": "temp/demais_atos.html",
#     "relatórios financeiros": "temp/relatorios.html",
#     "licitações": "temp/gestao.html",
#     "contratos": "temp/gestao.html",
#     "recursos humanos": "temp/rh.html",
#     "salário": "temp/rh.html",
#     "pagamento": "temp/rh.html",
#     "despesas": "temp/receitas_despesas.html",
#     "pauta": "temp/gestao.html",
#     "atas": "temp/gestao.html",
#     "sessões": "temp/gestao.html",
#     "leis": "temp/demais_atos.html",
#     "lei": "temp/demais_atos.html",
#     "atricom": "temp/demais_atos.html",
#     "obras": "temp/demais_atos.html",
#     "decretos": "temp/demais_atos.html",
#     "somos": "temp/gestao.html",
#     "você": "temp/gestao.html",
#     "conhecimento": "temp/gestao.html",
#     "fale": "temp/gestao.html",
# }

# Função que identifica o tema
# def identificar_tema(pergunta):
    # nlp = spacy.load("pt_core_news_sm")
    # doc = nlp(pergunta.lower())
    
    # for token in doc:
    #     if token.lemma_ in Temas:
    #         return token.lemma_
    # return None

# @api_view(['GET'])
# def menu_completo(request, id, pergunta):
    # Inicializa o modelo
    # chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    
    # # Identifica o tema com base na pergunta
    # tema = identificar_tema(pergunta)
    
    # if tema and tema in Temas:
    #     template_correto = Temas[tema]
    # else:
    #     return Response({'Erro': 'Tema não identificado na pergunta.'}, status=400)
    
    
    # # Carrega o HTML baseado no endpoint identificado
    # html = render_to_string(template_correto, {'id': id})

    # # Configura o template de prompt para o ChatGroq
    # template = ChatPromptTemplate.from_messages([
    #     ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {template_correto}"),
    # ("user", "{input}")
    # ])

    # chain = template | chat

    # # Limita o HTML para evitar excesso de caracteres
    # html = html[:4000]

    # # Tenta gerar a resposta
    # try:
    #     resposta = chain.invoke({'template_correto': html, 'input': pergunta})
    #     return Response({'Resposta': resposta.content}, status=200)
    # except Exception as e:
    #     return Response({'Erro': str(e)}, status=500)

#  Rota Index inicial
# def index(request):
    # return render(request, 'temp/index.html')

# Acessar Qualquer Página e ver por ID
# def gestao_api(request, id):
    # Passar o ID como parte do contexto para o template
    # context = {
    #     'id': id
    # }
    # return render(request, 'temp/gestao.html', context)

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

# Identificar sentido e palavra chave da pergunta
# @api_view(['GET'])
# def identifica_sentido(resquest, pergunta):
    chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview')
    if resquest.method == 'GET':
        template = ChatPromptTemplate.from_messages(
            [ ('system', 'Você é um especialista em gestão pública, com foco em transparência, finanças públicas e legislação municipal. Sua tarefa é analisar a frase fornecida pelo usuário e identificar a palavra ou palavras-chave que melhor descrevem o que o usuário deseja saber. Responda com clareza e concisão, retornando apenas a palavra-chave principal ou um conjunto de palavras relacionadas diretamente ao tema da frase. Não explique sua escolha, apenas forneça as palavras-chave. Exemplos: Entrada: "Quero ver os salários" Resposta: "salários". Entrada: "Quero saber onde ficam os contratos". Resposta: "contratos" Agora, identifique a palavra-chave da frase fornecida'),
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

@api_view(['GET'])
def menu_completo_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.3-70b-versatile')
    context = {
        'id': id,
        'link': 'https://it-solucoes.com/transparenciaMunicipal/'
    }
    html = render_to_string('temp/menu_resumido.html', context)

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, especializado em orientar os usuários a localizar informações em um portal com base em menus e links. Sua tarefa é analisar as perguntas recebidas, identificar o assunto principal e fornecer um passo a passo claro e detalhado para acessar as informações desejadas no portal. Instruções: 1. Leia atentamente a pergunta do usuário para identificar o assunto principal (ex.: remuneração, despesas, licitações). 2. Analise todas as seções e links disponíveis no documento HTML, priorizando aqueles mais relevantes ao tema da pergunta. 3. Organize sua resposta em um formato de passo a passo lógico e estruturado, descrevendo o caminho pelo menu e incluindo sempre o link da sessão idenficada. 4. A resposta deve ser clara, direta e formatada inteiramente em HTML, utilizando: - Uma <div> para conter o conteúdo. - Um <p> para cada passo, descrevendo as ações necessárias. - Os links em formato <a> com o texto clicável e o atributo href para a URL correspondente. 5. Garanta que a resposta seja fácil de compreender, sem menções técnicas como 'HTML', 'código', ou estruturas técnicas do documento. Formato da Resposta (em HTML): <div><p>1. Passo [Número]: [Descrição clara do que o usuário deve fazer].</p><p>- Link: <a href=\"[URL]\" title=\"[Descrição do link]\">[Texto do link]</a></p></div>. Regras: - Analise todas as seções do documento: Não limite sua busca à primeira seção encontrada; percorra todo o conteúdo. - Relacione diretamente a resposta ao tema da pergunta: Priorize títulos e descrições relevantes para encontrar a melhor correspondência. - Evite respostas genéricas ou desnecessárias: Não inclua links ou informações que não sejam diretamente úteis ao tema solicitado. - Caso não encontre informações relevantes: Informe que o dado solicitado não está disponível, formatando a mensagem dentro de uma <div> Sempre deve vir na resposta o link de acesso a sessão. E tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    # Você é um assistente chamado itAI, especializado em orientar os usuários a localizar informações em um portal com base em menus e links. Sua tarefa é analisar as perguntas recebidas, identificar o assunto principal e fornecer um passo a passo claro e detalhado para acessar as informações desejadas no portal. Instruções: 1. Leia atentamente a pergunta do usuário para identificar o assunto principal (ex.: remuneração, despesas, licitações). 2. Analise todas as seções e links disponíveis no documento HTML, priorizando aqueles mais relevantes ao tema da pergunta. 3. Organize sua resposta em um formato de passo a passo lógico e estruturado, descrevendo o caminho pelo menu e incluindo sempre o link da sessão idenficada. 4. A resposta deve ser clara, direta e formatada inteiramente em HTML, utilizando: - Uma <div> para conter o conteúdo. - Um <p> para cada passo, descrevendo as ações necessárias. - Os links em formato <a> com o texto clicável e o atributo href para a URL correspondente. 5. Garanta que a resposta seja fácil de compreender, sem menções técnicas como 'HTML', 'código', ou estruturas técnicas do documento. Formato da Resposta (em HTML): <div><p>1. Passo [Número]: [Descrição clara do que o usuário deve fazer].</p><p>- Link: <a href=\"[URL]\" title=\"[Descrição do link]\">[Texto do link]</a></p></div>. Regras: - Analise todas as seções do documento: Não limite sua busca à primeira seção encontrada; percorra todo o conteúdo. - Relacione diretamente a resposta ao tema da pergunta: Priorize títulos e descrições relevantes para encontrar a melhor correspondência. - Evite respostas genéricas ou desnecessárias: Não inclua links ou informações que não sejam diretamente úteis ao tema solicitado. - Caso não encontre informações relevantes: Informe que o dado solicitado não está disponível, formatando a mensagem dentro de uma <div> Sempre deve vir na resposta o link de acesso a sessão.
    #  Você é um assistente chamado itAI, especializado em orientar os usuários a localizar informações em um portal com base em menus e links. Sua tarefa é responder às perguntas fornecendo um passo a passo claro e objetivo para acessar as informações desejadas. Instruções: 1. Leia atentamente a pergunta do usuário para identificar o assunto principal (ex.: remuneração, despesas, licitações). 2. Procure no documento HTML as seções e links que sejam mais relevantes ao tema identificado. 3. Organize sua resposta em um passo a passo lógico, indicando o caminho dentro do menu e o link correspondente. 4. Forneça respostas claras e diretas, sem mencionar a estrutura HTML ou termos técnicos como 'HTML' ou 'código'. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link com a URL correspondente]. Regras: - Sempre relacione diretamente a resposta ao tema da pergunta. - Utilize os títulos e descrições das seções para contextualizar as instruções. - Evite mencionar termos técnicos desnecessários ou etapas genéricas sem conexão com a pergunta. - Se não houver informações relevantes no documento, informe claramente que o dado solicitado não está disponível.
    chain = template | chat

    html = html[:20000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
@api_view(['GET'])
def menu_completo_api_id_pref(request, id, pergunta, sigla):
    chat = ChatGroq(model='llama-3.3-70b-versatile')
    context = ''  
    html  = ''
    if sigla == 0:
        sigla = 'CM'
        context = {
        'id': id,
        'link': 'http://portaltransparencia.app.br/v3',
        'sigla': sigla
        }
        html = render_to_string('temp/menu_resumido.html', context)
    elif sigla == 1:
        sigla = 'PM'
        context = {
        'id': id,
        'link': 'http://portaltransparencia.app.br/v3',
        'sigla': sigla
        }
        html = render_to_string('temp/menu_resumido_pref.html', context)
    elif sigla == 2:
        sigla = 'FM'
        context = {
        'id': id,
        'link': 'http://portaltransparencia.app.br/v3',
        'sigla': sigla
        }
        html = render_to_string('temp/menu_resumido_fm.html', context)
    # end if
   
    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, especializado em orientar os usuários a localizar informações em um portal com base em menus e links. Sua tarefa é analisar as perguntas recebidas, identificar o assunto principal e fornecer um passo a passo claro e detalhado para acessar as informações desejadas no portal. Instruções: 1. Leia atentamente a pergunta do usuário para identificar o assunto principal (ex.: remuneração, despesas, licitações). 2. Analise todas as seções e links disponíveis no documento HTML, priorizando aqueles mais relevantes ao tema da pergunta. 3. Organize sua resposta em um formato de passo a passo lógico e estruturado, descrevendo o caminho pelo menu e incluindo sempre o link da sessão idenficada. 4. A resposta deve ser clara, direta e formatada inteiramente em HTML, utilizando: - Uma <div> para conter o conteúdo. - Um <p> para cada passo, descrevendo as ações necessárias. - Os links em formato <a> com o texto clicável e o atributo href para a URL correspondente. 5. Garanta que a resposta seja fácil de compreender, sem menções técnicas como 'HTML', 'código', ou estruturas técnicas do documento. Formato da Resposta (em HTML): <div><p>1. Passo [Número]: [Descrição clara do que o usuário deve fazer].</p><p>- Link: <a href=\"[URL]\" title=\"[Descrição do link]\">[Texto do link]</a></p></div>. Regras: - Analise todas as seções do documento: Não limite sua busca à primeira seção encontrada; percorra todo o conteúdo. - Relacione diretamente a resposta ao tema da pergunta: Priorize títulos e descrições relevantes para encontrar a melhor correspondência. - Evite respostas genéricas ou desnecessárias: Não inclua links ou informações que não sejam diretamente úteis ao tema solicitado. - Caso não encontre informações relevantes: Informe que o dado solicitado não está disponível, formatando a mensagem dentro de uma <div> Sempre deve vir na resposta o link de acesso a sessão. E tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
    chain = template | chat

    html = html[:20000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu Gestão
# @api_view(['GET'])
# def gestao_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/gestao.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
 
# Menu Receitas e Despesas   
# @api_view(['GET'])
# def receitas_despesas_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/receitas_despesas.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu Planejamento
# @api_view(['GET'])
# def planejamento_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/planejamento.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu Relatórios    
# @api_view(['GET'])
# def relatorios_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/relatorios.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)

# Menu RH 
# @api_view(['GET'])
# def rh_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/rh.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
    
# Menu Demais Atos   
# @api_view(['GET'])
# def demais_atos_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/demais_atos.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)
     
# Menu Legislativo  
# @api_view(['GET'])
# def legislativo_api_id(request, id, pergunta):
    chat = ChatGroq(model='llama-3.2-11b-vision-preview')
    html = render_to_string('temp/legislativo.html', {'id':id})

    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente chamado itAI, responsável por buscar informações dentro de documentos HTML. Sua tarefa é analisar as informações contidas no documento e fornecer um passo a passo claro e detalhado para ajudar o usuário a localizar as informações desejadas. Instruções: 1. Analise o documento HTML para identificar o conteúdo relevante, incluindo títulos, descrições e links. 2. Organize o conteúdo em um formato de passo a passo que oriente o usuário de forma clara sobre como encontrar as informações. - Cada passo deve ser uma instrução simples e direta. - Inclua o texto do link (se disponível) e o endereço literal do atributo `href`. - Adicione descrições úteis para contextualizar cada passo. Formato da Resposta: 1. Passo [Número]: [Descrição clara do que o usuário deve fazer]. - Link: [Texto do link]. Regras Adicionais: - Se não houver links ou informações claras no documento HTML, informe ao usuário que os dados não estão disponíveis no formato esperado. - Sempre siga a sequência lógica do documento HTML para apresentar os passos de forma organizada. - Use títulos e descrições dos elementos HTML como contexto adicional, caso estejam presentes. - Certifique-se de que os passos sejam fáceis de entender e executar. e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}"),
    ("user", "{input}")
    ])
     
    chain = template | chat

    html = html[:4000]
    
    try:
        resposta = chain.invoke({'documentos_informados': html, 'input': pergunta})
        return Response({'Resposta': resposta.content}, status=200)
    except Exception as e:
        return Response({'Erro': str(e)}, status=500)


       

