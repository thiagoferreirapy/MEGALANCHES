from django.contrib import admin
from .models import Categorias, Lanches, ImageBurguer, Sobremesa, Acompanhamento, Bebidas,Extra, Pedido
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Lanches)
admin.site.register(ImageBurguer)
admin.site.register(Pedido)
admin.site.register(Sobremesa)
admin.site.register(Acompanhamento)
admin.site.register(Bebidas)
admin.site.register(Extra)