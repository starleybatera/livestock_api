from rest_framework import  serializers
from animais.models import Animal
from raca.models import Raca
from agrupamentos.models import Agrupamento
from historico.models import Historico


class AnimalSerializer(serializers.ModelSerializer):

    cod_raca = serializers.SlugRelatedField( queryset=Raca.objects.all(),slug_field='descricao' )
    cod_agrupamento = serializers.SlugRelatedField( queryset=Agrupamento.objects.all(),slug_field='identificacao' )
    cod_historico = serializers.SlugRelatedField( queryset=Historico.objects.all(),slug_field='descricao')
    data_historico = serializers.CharField(source='cod_historico.data',required = False)

    class Meta:
        model = Animal
        fields = ['id', 'identificacao', 'descricao', 'cod_raca', 'cod_agrupamento','cod_historico','data_historico']
        # fields = '__all__'
        
    # def create(self, validated_data):
    #     raca = Raca.objects.get(descricao=validated_data['descricao'])
    #     agrupamento = Agrupamento.objects.get(id=validated_data['cod_agrupamento'])
    #     historico = Historico.objects.get(id=validated_data['cod_historico'])
    #     animal  = Animal.objects.create(identificacao=validated_data['identificacao'], 
    #                                     descricao=validated_data['descricao'],
    #                                     raca_id=raca.id, 
    #                                     agrupamento_id = agrupamento.id, 
    #                                     historico_id = historico.id )
    #     return animal 

    
   