from rest_framework import viewsets
from rest_framework.response import Response
from core.models import FonteEnergia, TarifaEnergia, Consumo, Habitat
from core.serializers import FonteEnergiaSerializer, TarifaEnergiaSerializer, ConsumoSerializer, HabitatSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Define o número padrão de registros por página
    page_size_query_param = 'perPage'
    max_page_size = 100

class FonteEnergiaViewSet(viewsets.ModelViewSet):
    queryset = FonteEnergia.objects.all()
    serializer_class = FonteEnergiaSerializer

class TarifaEnergiaViewSet(viewsets.ModelViewSet):
    queryset = TarifaEnergia.objects.all()
    serializer_class = TarifaEnergiaSerializer

class HabitatViewSet(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

class ConsumoViewSet(viewsets.ModelViewSet):
    queryset = Consumo.objects.filter().order_by('-id')[:10]
    serializer_class = ConsumoSerializer
