"""
    Último dia do mês em ano bissexto
"""
"""
Você também pode utilizar a função 'monthrange' de 'calendar' para pegar o número do dia na semana (entre 0-6)
e último dia do mês (entre 28-31), exemplo:
"""

from calendar import monthrange
from datetime import datetime

"""
# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
"""

print(monthrange(2020, 2))

"""
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6).

Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:
"""

dia_semana, ultimo_dia = monthrange(2020, 2)
print(f'O último dia de fevereiro de 2020 é o dia {ultimo_dia}')

"""
Você também pode criar uma lista, assim como mdays, contendo todos os últimos dias de meses do ano atual:
"""

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
