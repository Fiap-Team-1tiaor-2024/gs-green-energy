from rest_framework import viewsets
from rest_framework.response import Response
from core.models import FonteEnergia, TarifaEnergia, Consumo, Habitat
from core.serializers import FonteEnergiaSerializer, TarifaEnergiaSerializer, ConsumoSerializer, HabitatSerializer

class FonteEnergiaViewSet(viewsets.ModelViewSet):
    queryset = FonteEnergia.objects.all()
    serializer_class = FonteEnergiaSerializer

class TarifaEnergiaViewSet(viewsets.ModelViewSet):
    queryset = TarifaEnergia.objects.all()
    serializer_class = TarifaEnergiaSerializer

class HabitatViewSet(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

"""
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Se você estiver usando paginação
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Sem paginação
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            'total': len(serializer.data)  # Ou você pode usar queryset.count()
        })

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'habitats': serializer.data}) 
"""
class ConsumoViewSet(viewsets.ModelViewSet):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
