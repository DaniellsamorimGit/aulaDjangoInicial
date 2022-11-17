# Descrição

## Aula didática de Django + MySQL + arquivos estáticos e de media
Material didatico com as configurações iniciais para criar um site Django, com integração com banco de dados MySQL, e configuracoes de arquivos estáticos e de media, onde iremos mostrar na home page imagens estáticas e imagens de media enviadas pelo usuário.

# Índice

* [Descrição](#descrição)
* [Configurações iniciais do django](#configurações-iniciais-do-django)

* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Desenvolvedor](#desenvolvedor)
* [Considerações Finais](#considerações-finais)
* [Tutorial Deploy](#tutorial-deploy)

# Configurações iniciais do django

### Instalar o Django no ambiente virtual
    pip install django
    
### Criando a pasta de projetos
    django-admin startproject (nomedoprojeto) . 
    
(Em nomeprojeto de um nome ao seu projeto e coloque o "." no final para criar na raiz)
- vai criar a pasta do seu projeto e o arquivo manage.py. O manage.py é quem gerencia a estrutura do projeto e dentro dele vai criar o arquivo wsgi.py é quem gerencia a parte de servidor, o urls gerencia os links do site, o settings.py quem diz onde vão ficar localizados as pastas, os arquivos e etc.

### Criando o server local
    python manage.py runserver
- Vai criar o link, com congratulations. link criado no localhost com endereço (http://127.0.0.1:8000)


<hr>


# Pronto criamos toda estrutura do django, agora vamos criar o app (funcionalidades do django) 
OBS: um projeto pode ter varios app's

    django-admin startapp (nomedafuncinalidade)
    
- Funcionalidade dentro de um projeto é o que queremos criar em termos de página HTTP e no banco de dados.
- Na criação da funcionalidade será criada o arquivo models.pyonde iremos definir as tabelas do nosso banco de dados.

<hr>

### Integração com banco de dados MySQL
- Por padrão o django cria o banco de dados sqlite3, para usar o banco de dados como Mysql modifique as configurações no arquivo setings.py e em DATABASES, modifique as configuações do Django para as configuações mostradas abaixo.

### Configurações MySQL 

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql', 	# default
		'NAME': 'Mysqlmusic', 			# nome do seu banco de dados
		'USER': 'xxxxxxxxxxxx', 		# usuario admin
		'PASSWORD': 'yyyyyyy', 			# senha admin
		'HOST':'localhost', 			# endereco do db (Encrontra-se no workbench)
		'PORT':'3306', 				# porta do db (Encrontra-se no workbench)
	    }
	}

### Importando a biblioteca de gerenciamento do MySQL
    pip install mysqlclient 

OBS: criar usuarios no django por padrao o django ja faz isso, temos que nos preocupar em criar o db somente para nosso app em si.




vamos criar o superuser (o adm do site)
antes de tudo rodar o: python manage.py migrate para migrar seu DB
	
    - python manage.py createsuperuser
    - crie o que é pedido (usuario, emaile senha)
    - agora vc ja pode logar no site com user superuser (django ja cria automaticamnte)
banco de dados ate o momento nao foi criado em models, vamos apenas acessar a pagina do adm no navegador em http://127.0.0.1:8000/admin


vamos conectar o app ao projeto: 
em settings ->  installed apps -> e criar uma linha com o nome do seu app assim -> 'nomedafuncinalidade',

exemplo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomedafuncinalidade',
]




agora na pasta do nosso projeto vamos definir o link que queremos definir para nossa funcionalidade (assim cada funcionalidade tem seu link proprio), para isso vamos criar um arquivo urls.py dentro da nossa pasta de funcionalidade, e na urls.py "que esta dentro do projeto" a gente aponta pra esse link (compplicado mas basicamente sera link apontando para outro link)

vamos la:
dentro da ulrs.py do projeto, vamos adicionar a biblioteca include, essa biblioteca vai incluir as bibliotecas da nossa funcionalidade:

	from django.urls import include 

feito isso vamos adicionar:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('nomefuncionalidade.urls')) #leia obs
]


#obs no link sem nada "/" direcione para a nomefuncionalidade.urls isso que esta acontecendo nesta linha


TUDO PRONTO AGORA PRIMEIRO PASSO É CRIAR NOSSAS TABELAS DENTRO DO MODELS
E IMPORTALA ISANDO MAKEMIGRATIONS E MIGRATE


DENTRO DE MODELS VAMOS IMPORTAR 
	 from django.db import models


e vamos criar nossas classes para cada tabela de banco de dados
exemplo:

LISTA_CATEGORIA= (
    ("forro", "Forró"),
    ("rock", "Rock"),
)

class Music(models.Model):
    artista = models.CharField(max_length=500)
    album = models.CharField(max_length=500)
    thumb = models.ImageField(upload_to='music_images/')
    #album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA,null=True,blank=True)


    # mudar o modo de exibição da string da classe para titulo do curso no admin
    def __str__(self):
        return (self.artista + " (" + self.album + ")")





agora vamos instalar o pillow, que faz todo tratamento de imagens
	pip install pillow



vamos rodar o migrate e o makemigrations, que atualiza nosso banco de dados:
	- python manage.py makemigrations
    - python manage.py migrate


Nossa tabela ainda nao aparece no admin, vamos criar dentro da pasta de funcionalidades em admin.py 

	from .models import Musica
	admin.site.register(Musica)


pronto, agora vamos criar nosso banco de dados, como estamos usando o banco de dados que nao é padrao do django, temos que criar na unha, pra isso vamos abrir o cmd do windows e digitar

	mysql -u root -p

	#vai pedir a senha do seu banco de dados
	show database #pra ver os bancosque tem criados
	crate database [nome do banco]
	show database de novo pra ver se foi criado

	
duvidas veja o Link de configuracos do banco de dados mysql:	
https://www.codigofluente.com.br/configurando-o-django-com-mysql-windows/

crie de novo o super user:
	python manage.py createsuperuser

agora pode ver sua tabela feita no adm do seu site:
	http://127.0.0.1:8000/admin




