from django import forms
from .models import Producto, Oferta , Comentario

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
    