from django.shortcuts import render
from rest_framework import viewsets
from imagens.models import Imagens
from imagens.models import Animal
from .serializers import ImagensSerializer



class ImagensViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer

