from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    Nombre =models.CharField(max_length=200)
    ciudad =models.CharField(max_length=200)
    cedula =models.CharField(max_length=200)
    telefono =models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=200)
    codigo_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha= models.CharField(max_length=200)
    descuento= models.IntegerField()
    nombre_mesero= models.CharField(max_length=200)


class factura(models.Model):
    numero_factura =models.CharField(max_length=200)
    fecha_factura = models.CharField(max_length=200)
    nombre_cliente = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)
    nit_empresa = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    precio_total = models.DecimalField(max_digits=9, decimal_places=2)


class producto(models.Model):
    codigo_producto = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)


class reserva(models.Model):
    email = models.EmailField(verbose_name='email address', unique=True, max_length=244, null=True)
    nombre_cliente = models.CharField(max_length=200, null=True)
    fecha = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    numero_personas = models.CharField(max_length=200, null=True)

    def __str__(self):
        self.email


class mesa(models.Model):
    numero_mesa = models.IntegerField()
    cantidad_Sillas = models.IntegerField()

class provedores(models.Model):
    codigo_provedor = models.CharField(max_length=200)
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class stock(models.Model):
    codigo_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
