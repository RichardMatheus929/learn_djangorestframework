from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacoes
# Create your models here.
class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField()
    atracoes = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacoes)

    def __str__(self) -> str:
        return self.nome
