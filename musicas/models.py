from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIA= (
    ("forro", "Forró"),
    ("rock", "Rock"),
)


class Musica(models.Model):
    artista = models.CharField(max_length=500)
    album = models.CharField(max_length=500)
    thumb = models.ImageField(upload_to='img_dentro_de_media/')
    #album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA,null=True,blank=True)


    # mudar o modo de exibição da string da classe para titulo do curso no admin
    def __str__(self):
        return (self.artista)