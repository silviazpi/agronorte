from django.contrib import admin
from .models import Producto, Chollo, Documento, Noticia

class ProductosAdmin(admin.ModelAdmin):
    list_display=("nombre", "marca", "categoria", "subcategoria")
    search_fields=("nombre", "marca")
    list_filter=("marca", "categoria", "subcategoria")

class OcasionAdmin(admin.ModelAdmin):
    pass

class DocumentoAdmin(admin.ModelAdmin):
    list_display=("titulo", "descripcion", "archivo")
    search_fields=("titulo", "archivo")

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Chollo, OcasionAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Noticia)