"""
    Associação - Python Orientado a Objetos
"""
from Aula_068.classes import Escritor
from Aula_068.classes import Caneta
from Aula_068.classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
print(escritor.nome, caneta.marca)
