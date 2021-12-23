from django.template import Library
from utils import utils


register = Library()


@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


@register.filter
def qtd_total_carr(carrinho):
    return utils.qtd_total_carr(carrinho)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)
