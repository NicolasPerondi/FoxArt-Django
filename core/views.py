from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from productos.models import Product


class ContactPage(TemplateView):
    template_name = "core/contacto.html"


class NosotrosPage(TemplateView):
    template_name = "core/nosotros.html"


class HomePage(ListView):
    model = Product
    template_name = "core/home.html"
