from rest_framework import  serializers
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico


class AnimalSerializer(serializers.ModelSerializer):
    raca = serializers.ReadOnlyField()
    agrupamento = serializers.ReadOnlyField()
    historico = serializers.ReadOnlyField()
    class Meta:
        model = Animal
        fields = ['id', 'identificacao', 'descricao','agrupamento','raca','historico']
        
