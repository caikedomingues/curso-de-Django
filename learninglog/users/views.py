
# Arquivo que irá conter todas as views do arquivo user.

# Views: Basicamente a view serve para criarmos toda a lógica dos
# templates HTML do sistema e suas requisições. As views também 
# atuam como intermediárias entre o modelo de dados (models) e os templates.

# Resumindo:As Views são funções ou classes que recebem requisições HTTP e retornam respostas HTTP, geralmente renderizando templates HTML com dados do modelo(classes criadas no arquivo models.py).

# Import da classe HttpResponseRedirect do módulo django.http:
# HttpResponseDirect é usada para criar uma resposta HTTP que
# redireciona o usuário para outra URL. É muito util quando
# você precisa redirecionar o usuário após uma ação bem-sucedida
# como um envio de formulário ou um logout.
from django.http import HttpResponseRedirect

# Import da função reverse do módulo urls: O reverse é usado para
# gerar URLS a partir dos nomes das rotas definidas em nosso arquivo
# urls.py. Em vez de codificar URLS diretamente em seu código, você
# usa o reverse para gerar URLS dinamicamente, o que torna o seu
# código mais flexivel e fácil de manter. Por exemplo, se você alterar
# a URL de uma rota, não precisará atualizar todos os links em seu
# aplicativo.
from django.urls import reverse

# Import da função logout do módulo django.contrib.auth: O logout é
# uma função fornecida pelo Django que encerra a sessão de um usuário
# autenticado. Ela limpa os dados de autenticação do usuário e o desloga
# do sistema.
from django.contrib.auth import logout

# Import da função render do módulo django que tem como objetivo
# renderizar/criar templates HTML. A função render do Django é usada para criar e retornar respostas HTTP que contêm o conteúdo de um template HTML renderizado.
from django.shortcuts import render

# Import da função login do módulo django.contrib.auth: A função
# login é usada para iniciar uma sessão de usuário no Django. Ela
# armazena as informações de autenticação do usuário na sessão, 
# permitindo que o usuário acesse as áreas protegidas do sistema.
from django.contrib.auth import login

# Import da função authenticate do módulo django.contrib.auth:
# A função authenticate é usada para verificar as credenciais de
# um usuário (geralmente nome de usuário e senha) em relação ao banco de # dados do usuário do django. Se as credenciais forem válidas,
# authenticate retorna um objeto de usuário; caso contrário, retorna None.
from django.contrib.auth import authenticate

# Import da classe UserCreationForm do módulo django.contrib.auth:
# UserCreationForm é um formulário pré-construido fornecido pelo
# Django que simplifica a criação de novos usuários no sistema.
# Ele inclui campos para nome de usuário e senha (e, opcionalmente,
# outros campos, dependendo da configuração do seu projeto). Este
# formulário já realiza a validação dos dados inseridos pelo usuário,
# como por exemplo, verificar se de usuário existe.
from django.contrib.auth.forms import UserCreationForm

# Criação da view que irá encerrar a sessão do usuário. A função
# irá receber como argumento apenas o request que lida com requisi
# ções.
def logout_view(request):
    """Faz logout do usuário"""    
    
    
    # Chamada da função logout que irá encerrar/limpar todas as requisi
    # ções do usuário logado.
    logout(request)
    
    # Após encerrar a sessão do usuário, o Http Response irá encaminha-lo
    # para a página inicial.
    return HttpResponseRedirect(reverse('index'))



# Criação da view que irá ser responsável por realizar inserções
# (requisições posts) de novos usuários no sistema. A função irá
# receber como parametro o request que realiza as requisições.
def register(request):
    
    """Registra um novo usuário"""
    
    # Verificando se a requisição feita é diferente do método POST,
    # que irá significar que é a primeira vez que o usuário estara
    # acessando a página.  
    if request.method != 'POST':
        
        # Cria\instãncia um formulário em branco. Esse formulário é usado para exibir os campos de registro (nome de usuário e senha)
        form = UserCreationForm()
    
    # Caso a requisição seja do tipo POST (inserção de dados)
    else:
        
        # Cria uma instância do formulário UserCreationForm com os dados
        # enviados pelo usuário(armazenados em request.POST). Lembrando
        # que a variavel data possibilita a realização de validações
        # adicionais antes de enviar os dados.
        form = UserCreationForm(data=request.POST)
        
        # Ira verificar se os dados passados são condizentes com as
        # regras definidas no forms.py
        if form.is_valid():
            
            # Atribuindo os dados salvos a uma variável
            new_user = form.save()
            
            # Autentica o usuário recém-criado usando a função authenticate. Os argumentos especificam os dados
            # inseridos pelos usuários.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            
            # Irá usar o objeto request e o usuário autenticado para #iniciar a sessão do usuário (login) após o registro.
            login(request, authenticated_user)
            
            # Redireciona o usuário para a página inicial após o registro bem-sucedido.
            return HttpResponseRedirect(reverse('index'))
    
    # Dicionário que irá possibilitar que o template HTML acesse
    # a variável da view   
    context = {'form': form}
    
    # Retorno da renderização com a requisição, o caminho do template
    # HTML e o dicionário context.
    return render(request, 'users/register.html', context)
     