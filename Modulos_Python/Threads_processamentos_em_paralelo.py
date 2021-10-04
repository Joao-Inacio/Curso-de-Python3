"""
    Threads - Executando processamentos em paralelo
"""
from time import sleep
from threading import Thread
from threading import Lock

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 10)
t2.start()

t3 = MeuThread('Thread 3', 15)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo', 5))
t1.start()
t2 = Thread(target=vai_demorar, args=('Olá mundo', 10))
t2.start()
t3 = Thread(target=vai_demorar, args=('Olá mundo', 15))
t3.start()

for i in range(50):
    print(i)
    sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo', 10))
t1.start()
t1.join()

print('Thread acabou')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque}')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    print(ingressos.estoque)
