from rest_framework import  serializers
from usuario_agrupamento.models import Usuario_Agrupamento
from usuario.models import Usuario
from agrupamentos.models import Agrupamento



class Usuario_AgrupamentoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField()
    agrupamento = serializers.ReadOnlyField()

    class Meta:
        model = Usuario_Agrupamento
        fields = ['id', 'usuario', 'agrupamento']

