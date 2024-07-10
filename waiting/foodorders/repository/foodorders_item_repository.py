from abc import ABC, abstractmethod


class FoodordersItemRepository(ABC):
    @abstractmethod
    def create(self, foodorders, food, foodprice, foodquantity):
        pass
