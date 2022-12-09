from django import forms
from .models import Product

class PageForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'precio']
        widgets ={
            'title' : forms.TextInput(attrs={'placeholder' : 'Nombre del Producto' }),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción'}),
            'precio': forms.TextInput(attrs={'placeholder': 'Precio del Producto'}),
        }
        labels = {
            'title' : '', 'description':'', 'image': '', 'precio': '',
        }

