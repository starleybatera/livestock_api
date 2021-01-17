from django.db import models
from animais.models import Animal

def upload_imagem(instance, filename):
    return f"{instance.id}.{filename}"

class Imagens(models.Model):
    path = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to=upload_imagem, blank=True, null=True)
    cod_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.path

    def animal(self):
        return self.cod_animal.descricao
