"""
    String - Template
"""
from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    hoje = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='João', data=hoje)

print(corpo_msg)
