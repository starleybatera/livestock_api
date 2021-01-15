from django.shortcuts import render
from rest_framework import viewsets
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer