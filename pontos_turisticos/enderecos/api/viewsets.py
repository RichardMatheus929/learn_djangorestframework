from rest_framework.viewsets import ModelViewSet
from enderecos.models import Enderecos
from .serializers import EnderecoSerializer
from rest_framework.response import Response
from rest_framework import status


class EnderecoViewset(ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecoSerializer