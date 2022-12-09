from django import template
from productos.models import Product

register = template.Library()


@register.simple_tag
def get_producto_list():
    productos = Product.objects.all()
    return productos
