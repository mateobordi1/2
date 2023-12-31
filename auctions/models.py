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
        return f"{self.id}: {self.titulo} {self.descripcion} {self.precioinicial}$  {self.categoria} {self.vendido} {self.vendedor}"

class Oferta(models.Model):
    oferta= models.IntegerField(default=False)
    producto_id= models.IntegerField()
    comprador_id= models.IntegerField(default=False)

    def __str__(self):
        return f"oferta:{self.oferta}$ producto_id:{self.producto_id} comprador_id:{self.comprador_id}"

class Comentario(models.Model):
    producto_id = models.IntegerField()
    comentador_id= models.IntegerField()
    comentario= models.CharField(max_length=1000)
    def __str__(self):
        return f"usuario que comento: {self.comentador_id} comentario:{self.comentario}"

class Seguimiento(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    en_seguimiento = models.BooleanField(default=True)

class Ganadores(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey('Producto', on_delete=models.CASCADE)
