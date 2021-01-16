from django.db import models
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico

class Animal(models.Model):
    identificacao =  models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    cod_raca = models.ForeignKey(Raca,related_name='raca', on_delete=models.CASCADE)
    cod_agrupamento = models.ForeignKey(Agrupamento, related_name='agrupamento',on_delete=models.CASCADE)
    cod_historico = models.ForeignKey(Historico, related_name='historico',on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacao

    def raca(self):
        return self.cod_raca.descricao

    def agrupamento(self):
        return self.cod_agrupamento.identificacao

    def historico(self):
        return self.cod_historico.descricao


