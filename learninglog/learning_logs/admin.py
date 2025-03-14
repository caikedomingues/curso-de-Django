
# Register your models here.

# Nesse arquivo, nos importamos modelos (tabelas) para o 
# painel administrador do sistema. Resumindo O principal objetivo do arquivo admin.py é registrar seus modelos (tabelas) para que eles apareçam no painel de administração do Django.
# Ao registrar um modelo, você permite que os administradores do sistema criem, leiam, atualizem e excluam registros desse modelo através da interface de administração.

# Nesse trecho vamos criar o import da nossa tabela para que ela apareça
# no painel administrador. Basicamente o trecho esta dizendo que queremos
# importar da pasta learning_mods o arquivo models que contém a classe Topic.
from learning_logs.models import Topic

# Vamos fazer o mesmo processo com a classe Entry, para que ela 
# apareça no painel administrativo
from learning_logs.models import Entry

# Esse trecho serve para importar o módulo admin do Django, que é 
# responsável por fornecer a funcionalidade do painel do Django.
# Este é um módulo que faz parte do "contrib" do Django, que significa
# "contribuições". Ele contém código que é fornecido pelo Django para
# funcionalidades comuns, como o painel de administração. O módulo
# admin fornece classes e funções que permitem que você registre seus
# modelos para que eles apareçam no painel de administração.
from django.contrib import admin


# admin.site: É uma instância da classe AdminSite, que é responsável
# por gerenciar o painel de administração do Django.

# register(Topic): Este método é usado para registrar um modelo no
# painel de administração. O método recebe como parâmetro a classe
# (tabela) que devc ser adicionada ao painel de administração.
admin.site.register(Topic)

# Vamos novamente usar o método register para adicionar a classe ao
# painel
admin.site.register(Entry)