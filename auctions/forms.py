from django import forms
from .models import Producto, Oferta , Comentario, Seguimiento

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields= '__all__'
    
class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields= '__all__'
    