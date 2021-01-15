from django.shortcuts import render
from rest_framework import viewsets
from historico.models import Historico
from .serializers import HistoricoSerializer


class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
