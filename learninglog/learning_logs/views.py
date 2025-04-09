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

# Import do arquivo que contem o banco de dados. Basicamete
# estamos dizendo que queremos acessar dentro do arquivo
# models(que esta dentro de learning_log, por isso usamos
# o ponto) a classe (tabela) Entry.
from .models import Entry

# Import da classe TopicForm do arquivo forms.py que irá 
# possibilitar a criação e manipulação de formulários web
# Observação: Usamos o ponto para importar arquivos que estão
# no mesmo diretório.
from .forms import TopicForm

# Esta linha importa a classe HttpResponseRedirect do módulo
# django.http. É uma classe do Django usada para redirecionar
# o navegador do usuário para uma URL diferente. Quando você
# deseja que o usuário seja levado para outra página após uma
# ação (como enviar um formulário com sucesso), nós usamos
# o HttpResponseRedirect.
from django.http import HttpResponseRedirect

# Esta linha importa a função reverse do módulo django.urls.
# Essa função permite gerar URLS a partir dos nomes das suas
# views (funções e classes que lidam com as requisições). Em
# vez de codificarmos URLS diretamente no código, usamos o
# reverse para gerar URLS dinamicamente, o que torna nosso
# código mais flexivel e fácil de manter.
from django.urls import reverse

# Import da classe EntryForms do arquivo forms.py que irá criar
# os formulários web
from .forms import EntryForm

# import da função login_requered do modulo contrib.auth.decorators
# Essa função permite que você bloqueie visualizações (views) que
# exigem que o usuário esteja autenticado(logado). Um decorador
# (decorators) em python é uma forma de modificar o comportamento
# de uma função. No Django, usamos decoradores para adicionar
# funcionalidades extras as views sem precisar precisar alterar
# seu código interno.
from django.contrib.auth.decorators import login_required

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


# Para utilizar a função basta, eu dar um @login_required 
# em cima das funções que eu quero restringir. O login_required
# basicamente verifica se o usuário está logado. Se não estiver,
# o django redireciona automaticamente o usuário para a página de
# login(que no nosso caso sera a rota /users/login que definimos no
# settings.py na raiz do projeto, a pasta learninglog).
@login_required

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

@login_required
# função que ira renderizar a página de tópicos especificos, só que
# dessa vez ela recebera 2 aegumentos: o request (para requisições) e
# o topic_id (que irá armazenar o id informado na rota)
def topic(request, topic_id):
        
        """Mostra um único assunto e todas as suas entradas"""

        # Como queremos pegar apenas os id dos dados, vamos 
        # usar o  método get que ira receber como argumento
        # a coluna id com o valor passado na rota.
        topic = Topic.objects.get(id = topic_id)

        # Como Topic é chave estrangeira da tabela Entry,
        # vamos usar a tabela topic para acessar a tabela 
        # Entry para ordenar os dados em ordem decrescente
        # (do mais recente ao mais antigo). O sinal - serve
        # para indicar ao order_by que ele deve organizar de
        # maneira inversa.
        entries = topic.entry_set.order_by('-date_add')
        
        # Após organizar os dados, vamos criar um dicionario que irá
        # conter o tópico e suas entradas. Usaremos essas variaveis
        # ('topic' e 'entries') para acessar os valores das tabelas
        # no HTML.
        context = {'topic': topic, 'entries': entries}
        
        # Retorno com a renderização do Template Html contendo a 
        # requisição, o caminho para o arquivo (em templates/learning_logs) e o dicionário com os valores
        return render(request, 'learning_logs/topic.html', context)

@login_required
# Função que irá verificar se a requisição POST (inserção de dados
# no servidor) foi realizada com sucesso. A função ira receber apenas
# o request como argumento para realizar a requisição.
def new_topic(request):
    
    """Adiciona um novo assunto."""
    
    # Basicaente iremos verificar se o método da requisição é diferente
    # de um método POST
    if request.method != 'POST':
        
        # nenhum dado submetido, cria um formulário 
        # em branco
        # Se o if for verdadeiro o Django irá instanciar um formulário
        # em branco.
        form = TopicForm()
    
    # Se o Metodo da requisição for um POST vamos processar a inserção
    # dos dados no banco.
    else:
        
        # Dados do POST submetidos, processa os dados
        
        # Iremos instanciar o formulário com o método POST do
        # argumento request (para inserir os dados)
        form = TopicForm(request.POST)
        
        # Aqui, vamos verificar se o tipo do dado que será inserido
        # é do tipo válido, ou seja, se o tipo do campo é condizente
        # com o dado informado pelo usuário
        if form.is_valid():
            
            # Se a validação estiver correta iremos salvar dados e concluir o envio da requisoção POST.
            form.save()
            
            # Esta parte cria uma instância de HttpResponseRedirect e 
            # a retorna. Isso instrui o Django a enviar uma resposta
            # de redirecionamento para o navegador do usuário.
            # O reverse serve para gerar a URL para a view chamada
            # 'topics' (nome da URL criada no arquivo urls.py). O
            # Django procura por uma URL com esse nome e retorna 
            # a URL correspondente.
            return HttpResponseRedirect(reverse('topics'))
    
    # Dicionário que irá receber os valores do formulário gerado
    # no template HTML.
    context = {'form': form}
    
    # Função que irá renderizar o template HTML, realizar as requisições e possibilitar o uso do dicionário context
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
# Função que irá inserir novas anotações no banco de dados.
# A função irá receber dois parametros: o request (para realizar
# as requisições HTTP) e o topic_id (que será o id do tópico rela
# cionado a anotação).
def new_entry(request, topic_id):
    
    """Acrescenta uma nova entrada para um assunto especifico"""
    
    # Como queremos relacionar a anotação com um tópico em especifico,
    # vamos pegar o id do assunto escolhido
    topic = Topic.objects.get(id=topic_id)
    
    # ira verificar se o método da requisição é diferente
    # do POST (Metodo para inserção de dados no servidor).
    if request.method != 'POST':
        
        # Nesse caso nenhum dado será submetido, iremos 
        # apenas criar o formulário em branco
        
        form = EntryForm()
    
    # Se a requisição for um POST
    else:
        
        # EntryForm: classe do formulário que será criado no projeto.
        
        # request.POST: Requisição post que irá inserir dados no banco 
        # de dados.
        
        # data: Como esse formulário não estará completo, vamos 
        # atribuir a função em uma vraiável, para que o POST
        # não aconteça assim que instanciarmos o formulário. 
        form = EntryForm(data = request.POST)
        
        # Irá verificar se o tipo dos dados informados é 
        # condizente com o tipo definido no formulário, ou seja,
        # ele verifica se os dados estão de acordo com as regras
        # definidas na classe EntryForms        
        if form.is_valid():
            
            # Se esse if for verdadeiro, este método save cria uma
            # nova instância do modelo de banco de dados associado
            # ao formulário, preenchendo os campos do modelo com os
            # dados do formulário. O argumento commit=False instrui
            # o Django a não salvar a nova entrada no banco de dados
            # imediatamente. Isso permite que você faça modificações
            # adicionais na instância do modelo antes de salva-la.
            # Isso nos permitira associar a anotação ao assunto, já
            # que a modificação adicional será justamente a relação 
            # da anotação com um tópico antes de salvar os dados.
            new_entry = form.save(commit=False)
            
            # Esta linha adiciona um valor ao campo topic da nova entrada. A variável tópic representa o tópico ao qual a
            # nova anotação pertence. Isso é muito importante para 
            # estabelecer o relacionamento entre entrada e tópico
            new_entry.topic = topic
            
            # Após todas as modificações adicionais, o save irá
            # salvar os dados no banco de dados
            new_entry.save()

            # HttpResponseRedirect: Esta função cria uma resposta HTTP
            # que redireciona o navegador de usuário para a URL gerada
            # pela função reserve. Isso significa que, após salvar a
            # nova entrada, o usuário é redirecionado para a página do
            # tópico ao qual a entrada foi adicionada.
            
            # reverse('topic', args=[topic_id]): Esta função inverte
            # o nome da URL 'topic' para a URL correspondentes, usando
            # o topic_id fornecido como argumento. Isso gera a URL para
            # a página de detalhes do tópico.
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    
    # Dicionário que irá possibilitar o nosso acesso aos dados no
    # template HTML.
    context = {'topic':topic, 'form':form, 'topic_id':topic_id}
    

    
    # Retorno do método que irá conter a requisição POST, o caminho
    # da página de novas entradas e o dicionário com os dados das tabelas
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
# Função que irá renderizar o formulário que terá como objetivo
# atualizar as anotações dos tópicos. A função receberá 2 argumentos
# o request (que irá executar as requisições no servidor) e o entry_id
# que irá identificar qual anotação estamos atualizando.
def edit_entry(request, entry_id):
    
    """Edita uma entrada existente"""
    
    # Ira coletar o id da anotação que será atualizada
    entry = Entry.objects.get(id=entry_id)
    
    # Como a tabela topic é chave estrangeira da tabela entry
    # Vamos relacionar as 2 tabelas para identificarmos os tópicos
    # que pertencem as anotações.
    topic = entry.topic
    
    # Verificação da requisição: Se a requisição for diferente de um
    # post
    if request.method != 'POST':
        
        # Cria uma instância do formulário EntryForm e a inicializa com
        # os dados do objeto entry existente. Isso preenche o formulário
        # com os valores atuais da anotação, permitindo que o usuário os 
        # edite.
        form = EntryForm(instance=entry)
    
    # Se a requisição for um post, o sistema salavará no banco de dados
    # as atualizações feitas pelos usuários.
    else:
        
        # Cria uma instância do formulário EntryForm, inicializando-a  com os dados do objeto entry existente e os dados enviados pelo usuário via request.POST.
        form = EntryForm(instance=entry, data=request.POST)
        
        # Irá verificar se os dados estão condizentes com as regras
        # definidas na classe EntryForm
        if form.is_valid():
            
            # Irá salvar os dados no banco de dados 
            form.save()

            # Redireciona o usuário de volta para a página do tópico
            # (topic) ao qual a anotação pertence, exibindo as alterações
            # salvas.
            # Reverse: Gera a url para a view 'topic' com o id do tópico
            # como argumento
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    # Dicionário que irá possibilitar que o template HTML acesse as
    # variáveis definidas na view
    context = {'entry':entry, 'topic':topic, 'form': form} 
    
    # Retorno da função render que irá conter a requisição, a rota
    # pro template HTML e o dicionário context
    return render(request, 'learning_logs/edit_entry.html', context)


    
    
    

    
    
