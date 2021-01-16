from django.db import models
from historico_tipo.models import Historico_Tipo

class Historico(models.Model):
    descricao = models.TextField(max_length=255)
    data = models.DateField('Data')
    cod_tipo = models.ForeignKey(Historico_Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    def tipo_historico(self):
        return self.cod_tipo.descricao       