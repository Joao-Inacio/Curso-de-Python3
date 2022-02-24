from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_number = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__result = User()

    @property
    def result(self):
        return_data = self.__result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self.__result.firstname = firstname

    def add_lastname(self, lastname):
        self.__result.lastname = lastname

    def add_age(self, age):
        self.__result.age = age

    def add_phone(self, phone):
        self.__result.phone_number.append(phone)

    def add_address(self, address):
        self.__result.addresses.append(address)


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('João', 'Inácio', 22)
    print(user1)
