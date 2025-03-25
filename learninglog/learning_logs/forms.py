
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

# import da classe Entry do arquivo models que esta aqui nesse
# mesmo diretório. A classe Entry representa o modelo de dados
# (a tabela) para anotações no banco de dados.
from .models import Entry

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
    


# Agora vamos criar um objeto (formulário) que irá inserir anotações
# referentes aos tópicos cadastrados no sistema. Ela também ira herdar
# a classe ModelForm da biblioteca Forms.
class EntryForm(forms.ModelForm):
    
    
    # A classe que meta é usada para fornecer metadados sobre
    # o formulário. É aqui que você especifica qual o modelo
    # de dados o formulário está associado e quais campos do
    # modelo devem ser incluidos no formulário.
    class Meta:
        
        # Esta linha instrui o Django a basear este formulário no
        # modelo Entry. Isso significa que o formulário terá
        # campos correspondentes aos campos definidos na classe
        # Entry em models.py.
        model = Entry 
        
        # Esta linha especifica quais campos do modelo Enry devem ser
        # incluidos no formulário. Neste caso, apenas o campo text
        # anotacao (coluna) será incluido. Isso significa que o formulário terá um campo para o usuário inserir o texto da
        # anotação
        fields = ['text_anotacao']
        
         
        # É usado para personalizar o rótulo (label) de um campo
        # de formulário especifico. No nosso caso o rótulo do
        # campo text_anotacao será vázio.
        labels = {'text_anotacao': ''}
        
        # Widgets: No Django Forms, o atributo widgets é um dicionário
        # que permite personalizar a forma como os campos do formulário 
        # são renderizados em HTML. Por padrão, o Django escolhe widgets
        # apropriados para cada tipo de campo (por exemplo, um campo de
        # texto simples é renderizado como um <input type = "text").
        # No entanto, você pode substituir esses widgets padrão para
        # obter um controle mais preciso sobre a aparência e o 
        # comportamento dos campos.
        
        # text_anotacao: Indica o campo que será utilizado no formulário
        
        # forms.Textarea: Aqui, estamos explicitamente definindo que
        # o widget para o campo text_anotacao deve ser um Textarea.
        # Isso garante que o campo seja renderizado como um textarea
        # em HTML, permitindo que os usuários insiram textos em várias
        # linhas.
        
        # attrs={'cols':80}: Este é o ponto crucial da personalização.
        # O argumento attrs é um dicionário que permite adicionar
        # atributos HTML ao widget. Nesse caso, estamos adicionando
        # o atributo cols com valor 80. O atributo HTML cols especifica
        # o numero de colunas visiveis em um textarea. Ao definir cols =
        # 80, estamos instruindo o navegador a renderizar o textarea com
        # largura suficiente para exibir aproxidamente 80 caracteres por
        # linha.
        widgets = {'text_anotacao': forms.Textarea(attrs={'cols': 80})}
        
    
    