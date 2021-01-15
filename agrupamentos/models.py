from django.db import models

class Agrupamento(models.Model):
    identificacao = models.CharField(max_length=255)

    def __str__(self):
        return self.identificacao

