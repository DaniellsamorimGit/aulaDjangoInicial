'''
Aqui criamos as buscas do nosso banco de dados, chamados de contexto,
assim podemos criar uma lista com objetos que queremos e usa-la
para devidos fins
'''

from .models import Musica

def lista_imagens(request):
    lista_image = []
    for urlimagem in Musica.objects.values_list('thumb'):
        lista_image.append(urlimagem[0])
        print(urlimagem[0])

    # lista_image2 = Musica.objects.all().values()
    # print("Mostra tupla: ", lista_image2)

    return {"lista_image": lista_image}