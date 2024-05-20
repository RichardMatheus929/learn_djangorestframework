from rest_framework.viewsets import ModelViewSet
from enderecos.models import Enderecos
from .serializers import EnderecoSerializer

class EnderecoViewset(ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer