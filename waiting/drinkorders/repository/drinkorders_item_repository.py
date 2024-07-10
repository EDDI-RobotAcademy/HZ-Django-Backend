from abc import ABC, abstractmethod


class DrinkordersItemRepository(ABC):
    @abstractmethod
    def create(self, drinkorders, drink, drinkprice, drinkquantity):
        pass
