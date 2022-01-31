from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','tfno')
    search_fields=('nombre','tfno')

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',)
    date_hierarchy='fecha'

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)