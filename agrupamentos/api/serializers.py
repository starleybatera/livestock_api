from rest_framework import  serializers
from agrupamentos.models import Agrupamento


class AgrupamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agrupamento
        fields = ['id', 'identificacao']

