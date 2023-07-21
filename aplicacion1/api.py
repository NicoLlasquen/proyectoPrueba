from .models import Proyecto
from rest_framework import viewsets, permissions
from .serializador import ProyectoSerializado


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializado
