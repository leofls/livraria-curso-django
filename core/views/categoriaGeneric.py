from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_field = "id"
    serializer_class = CategoriaSerializer