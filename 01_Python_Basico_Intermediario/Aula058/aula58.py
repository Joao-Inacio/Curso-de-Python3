"""
    Funções decoradoras e decoradores
"""
"""

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)

    return slave


@master
def fala_oi():
    print('Oi')


# fala_oi = master(fala_oi)
fala_oi()
"""
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        result = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return result

    return interna


@velocidade
def demora():
    for i in range(5):
        sleep(1)


demora()
