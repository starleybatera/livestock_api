from django.db import models

class Historico_Tipo(models.Model):
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.descricao