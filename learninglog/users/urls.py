

# Esse arquivo irá conter todas as rotas do app users

# Import da função path do módulo urls que tem como objetivo acessar
# as rotas do django.
from django.urls import path

# Essa linha importa o módulo views do aplicativo django.contrib.auth
# Este aplicativo fornece visualizações (views) pré-construidas para
# autenticação de usuários, como login e logout. Auth_views é o
# apelido do módulo views que ira conter as funções de autenticação 
# de usuários.
from django.contrib.auth import views as auth_views

# Import do aqruivo que conterá todas as views que as urls (definidas
# aqui) deverão acessar.
from . import views

# Lista que armazena todas as rotas do aplicativo users
urlpatterns = [
    
    # Login: Define a parte da URL que corresponde a esse padrão.
    # auth_views.LoginView.as_view(template_name='users/login.html'): 
    # especifica a visualização que será chamada quando essa URL for
    # acessada.
    
    # auth_views.LoginView: É uma visualização genérica fornecida pelo
    # Django para exibir um formulário de login.
    
    # .as_view(template_name='users/login.html'): Configura a visualização para usar o template HTML"users/login.html" para renderizar o formulário de login 
    # name: especifica o nome da rota com o objetivo de otimizar
    # o processo de acesso ao link, já que ao usar o nome da rota,
    # não precisamos copiar a URL inteira.
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    
    # Criação da rota para a view de logout
    
    path('logout', views.logout_view, name='logout'),
]   
