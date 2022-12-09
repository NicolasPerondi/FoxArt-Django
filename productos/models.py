from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    precio = models.CharField(max_length=10, verbose_name='Precio')
    image = models.ImageField(verbose_name="Imagen", upload_to="productos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
