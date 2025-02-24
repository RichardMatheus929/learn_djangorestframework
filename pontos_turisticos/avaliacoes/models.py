from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Avaliacoes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.TextField(null=True,blank=True)
    nota = models.DecimalField(max_digits=3,decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user.username) + " deu nota " + str(self.nota) 