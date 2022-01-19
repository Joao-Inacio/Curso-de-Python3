from django.template import Library
from utils import utils


register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco(val)


@register.filter
def qtd_total_carr(carrinho):
    return utils.qtd_total_carr(carrinho)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)
