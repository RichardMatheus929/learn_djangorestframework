from django.db import models

# Create your models here.
class Enderecos(models.Model):
    rua_ou_bairro = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True,blank=True)
    longitude = models.IntegerField(null=True,blank=True)


    def __str__(self) -> str:
        return str(self.pais) + " " + str(self.estado)