from abc import ABC, abstractmethod


class DrinkordersItemRepository(ABC):
    @abstractmethod
    def create(self, drinkorders, drink, price, quantity):
        pass
