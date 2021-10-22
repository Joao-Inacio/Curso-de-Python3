"""
    Datetime - Trabalhando com data e hora em Python
"""
from datetime import datetime, timedelta

data = datetime(2018, 4, 20, 10, 53, 20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data2 = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data2)

"""
strptime(str, fmt)
.strftime(fmt)
timestamp
fromtimestamp()
"""
data3 = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
data3 = data3 + timedelta(days=5)
print(data3.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('02/11/1998 03:15:28', '%d/%m/%Y %H:%M:%S')
d2 = data.strptime('13/09/2021 14:28:35', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(f'Você viveu {dif.days} Dias e {dif.total_seconds()} segundos')
print()

'2,00435.21861.11667'
