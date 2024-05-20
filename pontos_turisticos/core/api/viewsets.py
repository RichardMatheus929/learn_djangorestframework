from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontosTuristicosViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        aprovado = self.request.query_params.get('aprovado', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)
        if aprovado is not None:  # Para verificar se 'aprovado' está presente na query string
            # Convertendo 'aprovado' para booleano
            aprovado_bool = aprovado.lower() in ('true', '1', 't', 'yes')
            queryset = queryset.filter(aprovado=aprovado_bool)
        
        return queryset