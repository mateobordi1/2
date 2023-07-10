from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    precioinicial = models.IntegerField()
    precioactual = models.IntegerField(default="0") 
    imagenurl = models.CharField(max_length=100000)
    categoria = models.CharField(max_length=64)
    vendido = models.BooleanField(default=False)
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    precioactual = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.titulo} {self.descripcion} {self.precioinicial}$ {self.imagenurl} {self.categoria} {self.vendido} {self.vendedor}"

class Oferta(models.Model):
    oferta= models.IntegerField(default=False)
    producto_id= models.IntegerField()
    comprador_id= models.IntegerField(default=False)
