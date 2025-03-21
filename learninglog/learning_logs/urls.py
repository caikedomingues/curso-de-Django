

# Nesse arquivo irmeos definir os caminhos que queremos que o nosso
# sistema tenha, basicamente iremos definir aqui as rotas que o
# arquivo urls.py da pasta raiz deve seguir.

# Import dom path que serve para indicar o
# o caminho(rota/link) que o django deve executar.
# O include serve para incluirmos rotas e urls no
# nosso sistema.
from django.urls import path

# Vamos importar dessa mesma pasta (por isso
# usaremos o ".") o arquivo views.
from . import views


urlpatterns = [

    # Aqui basicamente, vamos verificar se a url raiz está vazia,
    # se ela estiver, vamos chamar o método index. Vamos passar
    # também o parâmetro name que irá receber como o valor o nome
    # 'index' que será a referência do nosso link no HTML, dessa
    # maneira não precisamos escrever a rota inteira nos templates
    # HTML.
    path('',views.index, name='index'),
    
    # Vamos criar mais uma rota para a view (página) que irá
    # apresentar os tópicos ja cadastrados no banco de dados.
    # Agora, sempre que colocarmos a palavra 'topics' após
    # a barra da url raiz, iremos acessar essa nova página.
    path('topics', views.topics, name='topics'),
    
    # Criação da rota que irá levar o usuário para  a página
    # de um tópico especifico. Para isso será necessário passar
    # como parametro o id do tópico que queremos acessar. Para
    # capturar o id, vamos criar na rota da página uma variável
    # que irá armazenar esses valores.
    path('topic/<topic_id>/', views.topic, name='topic'),
    
     # Vamos criar a rota do nosso formulário criado no arquivo
    # forms.py
    path('new_topic', views.new_topic, name='new_topic'),
    
    
    
    
    
]
