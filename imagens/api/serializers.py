from rest_framework import  serializers
from imagens.models import Imagens
from animais.models import Animal


class ImagensSerializer(serializers.ModelSerializer):
    animal = serializers.ReadOnlyField()

    class Meta:
        model = Imagens
        fields = ['id', 'imagem','animal']