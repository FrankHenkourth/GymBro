from django.db import models

# Create your models here.
class Membresia(models.Model):
    idmember = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()

class Clientes(models.Model):
    idcliente = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=70)
    fecha = models.DateTimeField(auto_now=True)
    idmember = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    password = models.CharField(max_length=15,default='changeme')#

class CellClient(models.Model):
    idcell = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    telefono = models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now=True)
    idcliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)


class Planes(models.Model):
    idplan = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    nombre_plan = models.CharField(max_length=200)
    descripcion_plan = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

class TipoPlan(models.Model):
    id_ty_plan = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    tipo = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now=True)
    idplan = models.ForeignKey(Planes, on_delete=models.CASCADE)

class ClientPlant(models.Model):
    id_clie_plan = models.BigAutoField(primary_key=True, unique=True, serialize=True)
    fecha = models.DateTimeField(auto_now=True)
    idplan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)