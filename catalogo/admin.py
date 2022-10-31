from django.contrib import admin
from .models import Product
# Register your models here.

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('create','update')

admin.site.register(Product,ProductAdmin)