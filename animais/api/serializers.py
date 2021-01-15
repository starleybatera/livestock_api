from rest_framework import  serializers
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'identificacao', 'descricao','cod_agrupamento','cod_raca','cod_historico']
        
