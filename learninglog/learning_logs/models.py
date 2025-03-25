from django.db import models

# Create your models here.

# Esse arquivo serve para manipular o banco de dados da
# aplicação.Quando você define um modelo no Django, você está essencialmente definindo a estrutura de uma tabela no banco de dados. Cada instância do modelo representa uma linha nessa tabela.


# Vamos primweiro criar uma classe

# Classe que irá representar os tópicos que o usuário
# irá criar no sistema para inserir anotações.
# A classe irá herdar métodos e atributos da classe
# models da biblioteca Model
class Topic(models.Model):
    
    """Um assunto sobre qual o usuário está aprendendo"""
    
    # Basicamente estamos criando uma coluna text que é do
    # tipo texto que pode receber apenas 200 caracteres.
    text = models.CharField(max_length=200)
    
    # Ira pegar a data e hora do sistema usando o argumento
    # auto_now_added = True dentro do método DateTimeField
    # da classe models. Basicamente ira criar a coluna que
    # contém a data da criação do tópico
    date_added = models.DateTimeField(auto_now_add=True)
    
    # Em python, um método especial (também conhecido como "método mágico") define como um objeto deve ser representado como uma string.
    # No contexto do Django models, o método __str__ é usado para fornecer uma representação legivel por humanos de uma instância do modelo.O método __str__ permite que você controle como essas instâncias são exibidas quando você as imprime ou as exibe em outros contextos (como no painel de administração do Django).

    def __str__(self):
        
        """Devolve uma representação em string do modelo"""
        
        # self: é uma referência á instância atual do modelo.
        # text: Acessa o valor do campo text.
        # return: Retorna o valor do campo text como a representação
        # em stringa da instância. Isso também permite que o dado
        # apareça em formato de texto no painel administrativo 
        return self.text
    
    # Agora que ja criamos a classe, vamos criar o banco de dados no terminal, lembrando que, antes de criarmos o banco de dados, nós
    # usamos no terminal o comando migrate para criar o arquivo db.sqlite que irá conter o nosso banco de dados. 
    # Usaremos o db browser sqlite para visualizar o banco de dados.


# Agora vamos criar classe que será a tabela de entradas, basicamente
# ela será o tema especifico de um determinado tópico (assunto que o
# usuário está aprendendo). Essa classe também ira herdar os metodos
# e atributos da classe models da biblioteca Model
class Entry(models.Model):
    
    """Algo especifico aprendido sobre um assunto"""
    
    # Como queremos que cada tema ou esteja relacionado a um tópico
    # vamos usar uma chave estrangeira para relacionar as 2 tabelas.
    # Para usar a chave vamos usar o  método ForeignKey da classe
    # models. Esse método ira receber como parametro a tabela que 
    # ele irá se relacionar e o on delete que ira definir a maneira
    # como os dados serão excluidos. No nosso caso, usaremos o 
    # Cascade como padrão de exclusão, com ele, ao excluir um
    # tópico, ele também ira excluir todos os temas relacionados a 
    # aquele tópico. 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    # Coluna do tipo texto que irá receber as anotações dos usuários
    text_anotacao = models.TextField()
    
    # Coluna que irá receber o horário da inserção ou da atualização do 
    # dado no banco de dados. Para isso vamos usar o DatetimeField da
    # classe models que irá receber como parametro o auto_now_add = True
    date_add = models.DateTimeField(auto_now_add=True)
    
    # Classe que ira conter a variável que tem como o valor o plural
    # de 'Entry'. Vamos criar classe por que caso a instância seja
    # inscrita no plural, o sistema irá adaptar a escrita do nome 
    # da classe 
    class Meta:
        
        verbose_name_plural = 'entries'
    
    # Agora vamos criar o método que mostra os dados em formato
    # de string no painel administrativo.
    def __str__(self):  
        
        # self: é uma referência á instância atual do modelo.
        # text_anotação: Acessa o valor do campo text_anotacao.
        # return: Retorna os 50 primeiros valores do campo 
        # text_anotacao como representação em string da instância. Isso também permite que o dado apareça em formato de texto no painel administrativo 
        return self.text_anotacao[:50] + '...'



