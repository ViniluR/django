from django.contrib import admin
# Register your models here.
from .models import *
class FabricanteAdmin(admin.ModelAdmin):
# Cria um filtro de hierarquia com datas
    search_fields = ('Fabricante',)
    date_hierarchy = 'criado_em'
    
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ('Produto',)
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Sem promoção'
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('Categoria',)
    date_hierarchy = 'criado_em'
    
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Usuario)