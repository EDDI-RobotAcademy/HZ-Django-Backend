from abc import ABC, abstractmethod


class FoodordersItemRepository(ABC):
    @abstractmethod
    def create(self, foodorders, food, price, quantity):
        pass
