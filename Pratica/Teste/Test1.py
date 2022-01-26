def maiuscular(texto):
    assert isinstance(texto, (str)), 'O texto tem que ser uma string'
    return texto.upper()

tex = input()
print(maiuscular(tex))
print(maiuscular(10))
