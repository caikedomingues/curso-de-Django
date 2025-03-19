

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
    
    
]
