from decimal import Decimal
from rest_framework import serializers
from core.models import FonteEnergia, TarifaEnergia , Habitat, Consumo

class FonteEnergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FonteEnergia
        fields = '__all__'

class TarifaEnergiaSerializer(serializers.ModelSerializer):
    fonte = FonteEnergiaSerializer(read_only=True)  # Serializer aninhado para exibir detalhes da fonte

    class Meta:
        model = TarifaEnergia
        fields = '__all__'

class HabitatSerializer(serializers.ModelSerializer):
    fonte = FonteEnergiaSerializer(read_only=True )  # Serializer aninhado para exibir detalhes da fonte

    class Meta:
        model = Habitat
        fields = '__all__'

class ConsumoSerializer(serializers.ModelSerializer):
    habitat = HabitatSerializer(read_only=False)
    tarifa = TarifaEnergiaSerializer(read_only=False)
    
    def create(self, validate_data):
        habitat = Habitat.objects.get(nome=validate_data['habitat']['nome'])
        tarifa = TarifaEnergia.objects.get(valor_tarifa=validate_data['tarifa']['valor_tarifa'])
        consumo_kwh = validate_data['consumo_kwh']
    
        return Consumo.objects.create(tarifa=tarifa, habitat=habitat, consumo_kwh=consumo_kwh).save()
        



    class Meta:
        model = Consumo
        fields = '__all__'
