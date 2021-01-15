from django.shortcuts import render
from rest_framework import viewsets
from agrupamentos.models import Agrupamento
from .serializers import AgrupamentoSerializer

class AgrupamentoViewSet(viewsets.ModelViewSet):
    queryset = Agrupamento.objects.all()
    serializer_class = AgrupamentoSerializer