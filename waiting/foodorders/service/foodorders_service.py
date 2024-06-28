from abc import ABC, abstractmethod


class FoodordersService(ABC):
    @abstractmethod
    def createFoodorder(self, accountId, foodorderItemList):
        pass
