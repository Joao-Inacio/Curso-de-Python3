from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    Twenty_percent = TwentyPercent()
    five_percent = CustomDiscount(99.8)

    order = Order(1000, Twenty_percent)
    print(order.total, order.total_with_discount)
    order = Order(1000, five_percent)
    print(order.total, order.total_with_discount)
