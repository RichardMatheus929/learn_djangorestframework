from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontosTuristicosViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # Filtrando apenas os PontosTuristicos que estão aprovados
        return PontoTuristico.objects.filter(aprovado=True) 