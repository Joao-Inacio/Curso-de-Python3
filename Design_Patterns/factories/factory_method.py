from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_clientes(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_clientes(self) -> None:
        print('Carro de luxo está busca o cliente...')


class CarroPopular(Veiculo):
    def buscar_clientes(self) -> None:
        print('Carro popular está busca o cliente...')


class MotoPopular(Veiculo):
    def buscar_clientes(self) -> None:
        print('Moto popular está busca o cliente...')


class MotoLuxo(Veiculo):
    def buscar_clientes(self) -> None:
        print('Moto de Luxo está busca o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_clientes(self):
        self.carro.buscar_clientes()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['luxo']

    print('ZONA NORTE')
    
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_clientes()

    print()

    print('ZONA SUL')

    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_clientes()
