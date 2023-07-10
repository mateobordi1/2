from django import forms
from .models import Producto, Oferta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'
    