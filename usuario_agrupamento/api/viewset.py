from django.shortcuts import render
from rest_framework import viewsets
from usuario_agrupamento.models import Usuario_Agrupamento
from .serializers import Usuario_AgrupamentoSerializer


class Usuario_AgrupamentoViewSet(viewsets.ModelViewSet):
    queryset = Usuario_Agrupamento.objects.all()
    serializer_class = Usuario_AgrupamentoSerializer