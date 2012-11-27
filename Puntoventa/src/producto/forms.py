from django import forms
from producto.models import Categoria,Productos


#forma rapida
class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
      
# fields = ('name', 'address', 'city', 'state_province','country','website')
 
class ProductosForms(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre', 'precio_venta', 'precio_compra')