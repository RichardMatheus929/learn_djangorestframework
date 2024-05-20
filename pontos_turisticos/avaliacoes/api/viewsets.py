from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacaoSerializer

class AvaliacaoViewset(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer