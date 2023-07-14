from django.contrib import admin

from .models import Producto , Oferta, Comentario, Seguimiento
# Register your models here.

admin.site.register(Producto),
admin.site.register(Oferta), 
admin.site.register(Comentario),
admin.site.register(Seguimiento)