# views: Em Django, o arquivo views.py é onde você define
# a lógica de negócios da sua aplicação web. Ele é responsável
# por:
# 1. Receber e processar requisições HTTP: Quando um usuário acessa
# uma URL do seu site, o Django encaminha a requisição para a view
# correspondente.
# 2. Interagir com o modelo de dados (Models): As views geralmente 
# interagem com os modelos de dados (definidos em models.py) para
# buscar,criar, atualizar ou excluir dados do banco de dados. Elas
# podem realizar consultas complexas ao banco de dados usando o
# ORM (Object-Relational Mapper) do Django.
# 3.Renderizar Templates HTML: As views são responsáveis por renderizar
# templates HTML, que são arquivos que definem a estrutura e o layout 
# das páginas web. Elas podem passar dados no banco de dados ou de 
# outras fontes para os templates , que serão exibidos na página web.
# 4. Retornar respostas HTTP: Após processar a requisição e renderizar
# o template (se necessário), a view retorna uma resposta HTTP para o
# navegador do usuário. A resposta pode ser uma página HTML, um arquivo
# JSON, uma imagem ou qualquer outro tipo de conteúdo.


# É uma ferramenta muito útil no Django para gerar respostas HTTP,
# que são o que o navegador da web recebe do servidor. Em termos
# simples, ela pega um modelo HTML (um arquivo com a estrutura da
# sua página web), combina com os dados que você deseja exibir e 
# retorna uma página web completa para o usuário.
from django.shortcuts import render


# Import do arquivo que contem o banco de dados. Basicamete
# estamos dizendo que queremos acessar dentro do arquivo
# models(que esta dentro de learning_log, por isso usamos
# o ponto) a classe (tabela) Topic.
from .models import Topic
# Create your views here.

# def index(request): Esta linha define a função chamada index.
# Em Django, as funções de view sempre recebem um objeto request
# como primeiro argumento. O objeto request contém informações sobre
# a requisição HTTP feita pelo usuário, como o método HTTP (GET, POST
# ,etc), os dados enviados pelo usuário e outros detalhes.
def index(request):
    
    
    """Página principal do learning_logs"""
    
    # Ira retornar a gunção render do Django para renderizar um 
    # template HTML e retornar a reposta HTTP para o navegador 
    # do usuário. O primeiro argumento é o objeto request, que
    # é necessário para que o Django possa processar a requisição
    # corretamente. O segundo argumento é o caminho para o template
    # HTML que será renderizado. O render lê o conteúdo do arquivo
    # index.html, processa o template, substituindo quaisquer
    # variáveis ou tags que de template por seus valores correspondentes
    # Retorna uma resposta HTTP contendo o HTML renderizado.
    return render(request, 'learning_logs/index.html')


# Função que irá renderizar o template html que irá conter os tópicos
# cadastrados no banco de dados. Vale lembrar que por padrão os métodos
# do view devem receber como argumento o "request" que possibilita que
# view realize requisições 
def topics(request):

    """Mostra todos os assuntos"""
    
    # Variável que ira conter a classe Topic que terá como objetivo
    # chamar o método objects.order_by que irá receber como argumento
    # o nome da coluna que será o padrão de organização dos dados.
    topics = Topic.objects.order_by('date_added')
    
    # Após a organização dos dados, vamos criar um dicionário
    # que terá como objetivo mostrar os dados cadastrados na
    # tabela Topic.
    context = {'topics':topics}
    
    # Por último vamos retornar o método render que ira conter o caminho
    # do template html (que estara na pasta templates/learning_logs)
    # e o request que fará a requisição. O render é responsável por 
    # renderizar a página HTML.Também retornaremos a variável context com
    # o objetivo de mostrar os seus valores na página.
    return render(request, 'learning_logs/topics.html', context)
    
    
