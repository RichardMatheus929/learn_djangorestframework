from django.db import models

from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos
# Create your models here.
class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=True)
    atracoes = models.ForeignKey(Atracao,on_delete=models.CASCADE,null=True,blank=True)
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE,null=True,blank=True)
    avaliacao = models.ForeignKey(Avaliacoes,on_delete=models.CASCADE,null=True,blank=True)
    endereco = models.ForeignKey(Enderecos,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.nome
