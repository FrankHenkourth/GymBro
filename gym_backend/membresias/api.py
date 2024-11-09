from membresias.models import Membresia, Clientes, CellClient, Planes, TipoPlan, ClientPlant
from rest_framework import viewsets, permissions
from .serializer import MembresiaSerializer, ClientesSerializer, CellClientSerializer, PlanesSerializer, TipoPlanSerializer, ClientPlantSerializer

class MembresiaViewSet(viewsets.ModelViewSet):
    queryset = Membresia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MembresiaSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientesSerializer

class CellClientViewSet(viewsets.ModelViewSet):
    queryset = CellClient.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CellClientSerializer

class PlanesViewSet(viewsets.ModelViewSet):
    queryset = Planes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlanesSerializer

class TipoPlanViewSet(viewsets.ModelViewSet):
    queryset = TipoPlan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoPlanSerializer

class ClientPlantViewSet(viewsets.ModelViewSet):
    queryset = ClientPlant.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientPlantSerializer
