from rest_framework import serializers
from .models import Membresia, Clientes, CellClient, Planes, TipoPlan, ClientPlant

class MembresiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membresia
        fields = ('idmember', 'nombre', 'descripcion', 'fecha')
        read_only_fields = ('idmember', 'fecha', )

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('idcliente', 'nombre', 'correo', 'idmember', 'fecha')
        read_only_fields = ('idcliente', 'fecha', )

class CellClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellClient
        fields = ('idcell', 'telefono', 'idcliente', 'fecha')
        read_only_fields = ('idcell', 'fecha', )

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ('idplan', 'nombre_plan', 'descripcion_plan', 'fecha' )
        read_only_fields = ('idplan', 'fecha', )

class TipoPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlan
        fields = ('id_ty_plan', 'tipo', 'idplan', 'fecha')
        read_only_fields = ('id_ty_plan', 'fecha', )

class ClientPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPlant
        fields = ('id_clie_plan', 'idcliente', 'idplan', 'fecha')
        read_only_fields = ('id_clie_plan', 'fecha', )
