from django.db import models

class Raca(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao