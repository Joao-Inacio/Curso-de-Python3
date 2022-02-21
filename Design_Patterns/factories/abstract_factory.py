from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_clientes(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_clientes(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_clientes(self) -> None:
        print('Carro de luxo ZN está busca o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_clientes(self) -> None:
        print('Carro popular ZN está busca o cliente...')


class MotoPopularZN(VeiculoPopular):
    def buscar_clientes(self) -> None:
        print('Moto popular ZN está busca o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_clientes(self) -> None:
        print('Moto de Luxo ZN está busca o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_clientes(self) -> None:
        print('Carro de luxo ZS está busca o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_clientes(self) -> None:
        print('Carro popular ZS está busca o cliente...')


class MotoPopularZS(VeiculoPopular):
    def buscar_clientes(self) -> None:
        print('Moto popular ZS está busca o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_clientes(self) -> None:
        print('Moto de Luxo ZS está busca o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()


class Cliente:
    def buscar_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_clientes()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_clientes()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_clientes()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_clientes()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.buscar_clientes()
