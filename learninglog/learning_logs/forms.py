
# Nesse arquivo iremos criar o formulário que irá possibilitar
# que o usuário insira anotações no banco de dados. Esse arquivo 
# sera baseado na classe Topic definida no arquivo models.py que
# tem como objetivo manipular o banco de dados do sistema.

# Esta linha importa o módulo forms do Django, que fornece as 
# ferramentas necessárias para criar formulários web dinâmico.
from django import forms

# import da classe Topic do arquivo models que esta aqui nesse
# mesmo diretório. A classe Topic representa  o modelo de dados
# (a tabela) para tópicos no banco de dados.
from .models import Topic

# Vamos definir uma nova classe chamada TopicForm que herda
# forms.ModelForm. ModelForm é uma classe especial do Django
# que permite criar formulários diretamente a partir de seus
# modelos de dados. Isso simplifica muito o processo de criação
# de formulários para manipulação de dados do banco de dados.
class TopicForm(forms.ModelForm):
    
    # A classe que meta é usada para fornecer metadados sobre
    # o formulário. É aqui que você especifica qual o modelo
    # de dados o formulário está associado e quais campos do
    # modelo devem ser incluidos no formulário.
    class Meta:
        
        # Esta linha instrui o Django a basear este formulário no
        # modelo Topic. Isso significa que o formulário terá
        # campos correspondentes aos campos definidos na classe
        # Topic em models.py.
        model = Topic
        
        # Esta linha especifica quais campos do modelo Topic devem ser
        # incluidos no formulário. Neste caso, apenas o campo text
        # (coluna) será incluido. Isso significa que o formulário
        # terá um campo para o usuário inserir o texto do tópico
        fields = ['text']
        
        # É usado para personalizar o rótulo (label) de um campo
        # de formulário especifico. No nosso caso o rótulo do
        # campo text será vázio.
        labels = {'text':''}
    
    