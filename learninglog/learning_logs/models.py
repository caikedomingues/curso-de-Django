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
        # em stringa da instância.
        return self.text
    
    # Agora que ja criamos a classe, vamos criar o banco de dados no terminal, lembrando que, antes de criarmos o banco de dados, nós
    # usamos no terminal o comando migrate para criar o arquivo db.sqlite que irá conter o nosso banco de dados. 
    # Usaremos o db browser sqlite para visualizar o banco de dados.