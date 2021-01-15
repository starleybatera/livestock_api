from rest_framework import  serializers
from imagens.models import Imagens
from animais.models import Animal


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = ['id', 'path', 'cod_animal']