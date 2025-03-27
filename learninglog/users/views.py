
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