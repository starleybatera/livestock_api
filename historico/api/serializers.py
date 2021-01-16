from rest_framework import  serializers
from historico.models import Historico
from historico_tipo.models import Historico_Tipo


class HistoricoSerializer(serializers.ModelSerializer):
    tipo_historico = serializers.ReadOnlyField()
    
    class Meta:
        model = Historico
        fields = ['id', 'descricao','data','tipo_historico']
        
