

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

# Vamos Adicionar isso para evitar conflitos de nomes de rotas
app_name = 'learning_logs'


urlpatterns = [

    path('',views.index),
    
    
]
