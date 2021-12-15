from django.contrib import admin
from . import models
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 0


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado',
                    'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
