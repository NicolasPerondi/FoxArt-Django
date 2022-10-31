from django.db import models
from turtle import title
from tabnanny import verbose
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    link = models.URLField(verbose_name="Dirección web", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="productos")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-create"]