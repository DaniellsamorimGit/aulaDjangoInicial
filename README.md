# Descrição

## Material didático de Django + MySQL + arquivos estáticos e de media
Material didático com as configurações iniciais para criação de sites com Django, integração com banco de dados MySQL e configurações de arquivos estáticos e de media (arquivos enviados pelos usuários).

# Índice

* [Descrição](#descrição)
* [Configurações iniciais do django](#configurações-iniciais-do-django)
* [Criando nosso APP](#criando-nosso-app)
* [Configurando MySQL](#configurando-mysql)
* [Criando o super user](#criando-o-super-user)
* [Configurações básicas finais](#configurações-básicas-finais)
* [Configurando arquivos estáticos e de media](#configurando-arquivos-estáticos-e-de-media)

<hr>

# Configurações iniciais do django

### Instalando Django no ambiente virtual
    pip install django
    
### Criando a pasta de projetos
    django-admin startproject (nomedoprojeto) . 
    
- Em nomeprojeto de um nome ao seu projeto e coloque o "." no final para criar na raiz.
- vai criar a pasta do seu projeto e o arquivo manage.py. O manage.py é quem gerencia a estrutura do projeto e dentro dele vai criar o arquivo wsgi.py é quem gerencia a parte de servidor, o urls gerencia os links do site, o settings.py quem diz onde vão ficar localizados as pastas, os arquivos e etc.

### Criando o server local
    python manage.py runserver
- Vai criar o link, com congratulations. link criado no localhost com endereço (http://127.0.0.1:8000)
- Pronto, a estrutura principal do DJANGO foicriada.

<hr>


# Criando nosso APP 
App é a funcionalidade do nosso site, como por exemplo server de músicas, pode ter "cadastro de artistas", "cadastro de músicas" e etc...

    django-admin startapp (nomedafuncinalidade)
    
- Funcionalidade dentro de um projeto é o que queremos criar em termos de página HTTP e no banco de dados.
- Na criação da funcionalidade será criada o arquivo models.py onde iremos definir as tabelas do nosso banco de dados.

<hr>

# Configurando MySQL
Por padrão o django cria o banco de dados sqlite3, para usar o banco de dados como Mysql modifique as configurações no arquivo setings.py e em DATABASES, mude as configuações do Django para as configuações do seu banco, como no exemplo abaixo.

### Configurações MySQL 

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql', 	# default
		'NAME': 'sqlmusic', 			# nome do seu banco de dados
		'USER': 'xxxxxxxxxxxx', 		# usuario admin
		'PASSWORD': 'yyyyyyy', 			# senha admin
		'HOST':'localhost', 			# endereco do db (Encrontra-se no workbench)
		'PORT':'3306', 				# porta do db (Encrontra-se no workbench)
	    }
	}

### Importando a biblioteca de gerenciamento do MySQL
    pip install mysqlclient 

- OBS: O django ja gerencia por si a página admin do site e a criação de novos usuários em (http://127.0.0.1:8000/admin)

### Agora vamos criar nossas tabelas dentro do models.py

- Dentro de models.py importe 
    
      from django.db import models
    
- Criando as classes para nossas tabelas (essa será nossa tabela no mysql)
-

	LISTA_CATEGORIA= (
	    ("forro", "Forró"),
	    ("rock", "Rock"),
	)

	class Musica(models.Model):
	    artista = models.CharField(max_length=500)
	    album = models.CharField(max_length=500)
	    thumb = models.ImageField(upload_to='music_images/')
	    #album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
	    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA,null=True,blank=True)


	    # mudar o modo de exibição da string da classe para titulo do curso no admin
	    def __str__(self):
		return (self.artista + " (" + self.album + ")")

### Criando o banco dentro do MySQL

O django não cria o banco Mysql automaticamente como acontece com sqlite padrão do django, pra isso temos que criar manualmente usando o PROMPT do windows ou no Workbench. Abra o CMD e digite:

    mysql -u root -p
Vai pedir a senha do seu banco de dados.

    show database 
Mostra os bancos que tem criados no MySql.

    create database [nome do banco]
Cria o banco com o mesmo nome dado nas configurações do Mysql em DATABASE -> NAME (sqlmusic). Para confirmar rode -show database.

	
- Dúvidas veja o Link de configuracos mais detalhadas:	<br>
https://www.codigofluente.com.br/configurando-o-django-com-mysql-windows/



### Migrando as tabelas

No terminal rode o migrate e o makemigrations, que cria nossas tabelas com base no arquivo models.py.

      python manage.py makemigrations
      python manage.py migrate
- Se tudo deu certo, agora suas tabelas foram criadas em seu database.
- 


### Configurando nossa tabela no ADMIN
Nossa tabela ainda nao aparece no admin, vamos adicionar dentro da pasta de (funcionalidades) em admin.py:

    from .models import Musica
    admin.site.register(Musica)
- Onde 'Musica' é o nome da tabela criada dentro de models.py.

<hr>

# Criando o super user 
Super user é o administrador do site, aquele com todasas permissões.

    python manage.py createsuperuser
	
- Crie seu usuario e senha.
- Agora pode ver sua tabela feita no adm do seu site em (http://127.0.0.1:8000/admin)


### instalando pillow
Pillow faz parte da biblioteca PIL de Imagens do Python, é um pacote que expõe muitas funções para manipular imagens a partir de um script Python.

    pip install pillow


<hr>

# Configurações básicas finais

### Conectando o app ao projeto
Em settings ->  installed apps -> crie uma linha com o nome do seu app (nomedafuncinalidade)


	Exemplo:
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'nomedafuncinalidade',
	]



<hr>

### Criando links do projeto
No projeto temos a pasta urls.py, ela quem comanda todos os links criados dentro do projeto (inclusive urls para as imagens e arquivos do projeto), e para cada funcionalidade podemos criar tbm um novo arquivo urls.py com os links desta funcionalidade mas para isso precisamos apontar dentro da urls.py do projeto para as outras urls (sim, urls apontanto para outras urls).
<br>
Vamos ver o que há na pasta urls.py do projeto:

	urlpatterns = [
	    path('admin/', admin.site.urls),
	]
- Temos o caminho 'admin/' para a url de admin do nosso site.

Vamos criar a urls.py para nossafuncionalidade (musica), pra isso entre na pasta da sua funcionalidade e crie o arquivo urls.py, não faremos nada ainda, apenas vamos apontar o projeto para essa url, pra isso,dentro de urls.py do projeto importe:

    from django.urls import include 
Agora vamos apontar para a url da funcionalidade acrescentando a linha abaixo:

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('/', include('nomefuncionalidade.urls')) #leia obs
	]
Pronto, agora esta feito o link do projeto para os links das suas funcionalidades, e la dentro vc poderá criar as urls das suas páginas. Vamos configurar agora os arquivos estáticos e mais a frente faremos nossa primeira página funcional.

<hr>

# Configurando arquivos estáticos e de media
Antes de criar nossa primeira página em si, vamos configurar os arquivos estáticos e de media, os arquivos estaticos são aqueles quenão mudam no nosso site, são fixos, como as imagens de fundo por exemplo, ja arquivos de media são arquivos dinâmicos, que podem mudar constantemente em nosso site como por exemplo a foto de um perfil de um usuário.

Vamos configurar tudo no arquivo settings.py:

### Crie a url para seus arquivos:

    STATIC_URL = 'static/'

### Especifique o local da sua pasta de arquivos staticos:

	STATICFILES_DIRS = [
	    BASE_DIR / 'static'
	]

Obs: Onde BASE_DIR é o local do seu projeto (ou seja a pasta de suas imagens vai está na mesma pasta do seu projeto), então crie na raiz do seu projeto essa pasta chamada 'static' (pode ser qualquer nome mas por default chamamos de static), sua pasta deve aparecer como na imagem abaixo:

![Captura de tela 2022-11-18 085643](https://user-images.githubusercontent.com/115194365/202700119-f2fd46d3-43d2-4694-b974-94081d569431.png)














como dito anteriormente, a pasta static é onde ficam os arquivos css,
arquivos javascript e as imagens, entao crie dentro dessa pasta static, outras pastas chamadas css, js e image (não é obrigatorio mas por organização)


agora dentro da pasta do seu projeto, em urls.py adicione a linha

	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

e importe la dentro:
	from django.conf import settings
	from django.conf.urls.static import static

isso vai garantir o roteamento para suas pastas statics






AGORA VAMOS CONFIGURAR OS ARQUIVOS MEDIA (SAO ARQUIVOS NAO ESTATICOS, QUE OS USUARIOS PODEM MANDAR PARA O SITE COMO FOTO DE PERFIL POR EXEMPLO)

Pra isso adicione em urls.py do seu projeto a linha:

	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

Agora vamos definir em settings essas variaveis de media ne?

	MEDIA_URL = 'media/'
	MEDIA_ROOT = BASE_DIR / 'media'

pronto, agora se vc subir uma imagem no banco de dados, vai salvar o caminho
na pasta media ou na pasta static




























