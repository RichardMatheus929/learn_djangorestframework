from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework import filters


class AtracoeViewset(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # Forma do chave=valor
    filterset_fields  = ['nome','horario_func','idade_min']

    # forma do search=valor_de_qualquer_chave
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'nome',
        'descricao',
        'horario_func',
        'idade_min' # Pesquisando dentro de Pontos_turisticos a chave nota da chave estrangeria avaliacao
        ]