from rest_framework.serializers import ModelSerializer
from enderecos.models import Enderecos

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('rua_ou_bairro','logradouro','cidade','estado','pais')