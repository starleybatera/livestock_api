from django.db import models
from usuario.models import Usuario
from agrupamentos.models import Agrupamento


class Usuario_Agrupamento(models.Model):
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cod_agrupamento = models.ForeignKey(Agrupamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_usuario

    def usuario(self):
        return self.cod_usuario.nome

    def agrupamento(self):
        return self.cod_agrupamento.identificacao