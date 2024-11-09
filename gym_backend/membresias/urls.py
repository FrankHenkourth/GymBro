from django.urls import path, include
from rest_framework import routers
from .api import CellClientViewSet, PlanesViewSet, ClientesViewSet, TipoPlanViewSet, MembresiaViewSet, ClientPlantViewSet
from .views import *


#router = routers.DefaultRouter()

# Agrega los routers para cada conjunto de vistas
#router.register(r'cellclients', CellClientViewSet, basename='cellclients')
#router.register(r'planes', PlanesViewSet, basename='planes')
#router.register(r'clientes', ClientesViewSet, basename='clientes')
#router.register(r'tipoplan', TipoPlanViewSet, basename='tipoplan')
#router.register(r'membresia', MembresiaViewSet, basename='membresia')
#router.register(r'clientplants', ClientPlantViewSet, basename='clientplants')

# Agrega los routers a la ruta principal
urlpatterns = [
   
]