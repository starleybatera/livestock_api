from django.db import models
from animais.models import Animal


class Imagens(models.Model):
    path = models.CharField(max_length=255)
    cod_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.path
