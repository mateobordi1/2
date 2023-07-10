from django.contrib import admin

from .models import Producto , Oferta, Comentario
# Register your models here.

admin.site.register(Producto),
admin.site.register(Oferta), 
admin.site.register(Comentario)