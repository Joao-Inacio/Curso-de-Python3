from pessoa import Pessoa

p1 = Pessoa('Luiz', 34)
p2 = Pessoa('João', 24)

p1.comer('Maçã')
p1.parar_comer()
p2.comer('Uvá')
p2.parar_comer()

p1.falar('Pergunta')
p2.falar('Resposta')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
