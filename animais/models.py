from django.db import models
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico

class Animal(models.Model):
    identificacao =  models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    cod_raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    cod_agrupamento = models.ForeignKey(Agrupamento, on_delete=models.CASCADE)
    cod_historico = models.ForeignKey(Historico, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacao

    

