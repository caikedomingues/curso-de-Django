"""
URL configuration for learninglog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Ese arquivo irá possuir as urls que o desenvolvedor pode
# acessar no desenvolvimento da aplicação. O arquivo urls.py
# é responsável por mapear URLs (endereços web) para as views
# (funções ou  classes) correspondentes no seu aplicativo 
# Django. Quando um usuário acessa uma URL no seu site, o
# Django usa o urls.py para determinar qual view deve ser
# executada para processar a solicitação.

# Import do painel administrativo do django
from django.contrib import admin

# Import dom path que serve para indicar o
# o caminho(rota/link) que o django deve executar.
# O include serve para incluirmos rotas e urls no
# nosso sistema.
from django.urls import path, include

urlpatterns = [
    
    # URL para administradores (desenvolvedores) do sistema
    # acessarem o painel administrativo do django.
    path('admin/', admin.site.urls),
    
    # Aqui basicamente vamos adicionar o caminho do aplicativo 
    # como padrão, ou seja, quando a  raiz não tiver mais 
    # nada após a barra, o sistema ira direcionar o django
    # para o nosso sistema. Para realizae essa ação, primeiro
    # vamos verificar se a url está vazia, caso ela esteja vazia
    # iremos passar para o include o caminho do arquivo urls.py
    # da pasta do aplicativo leaning.logs. 
    path('', include('learning_logs.urls'))
   
]
