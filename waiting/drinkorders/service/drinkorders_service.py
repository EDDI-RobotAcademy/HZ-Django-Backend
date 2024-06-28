from abc import ABC, abstractmethod


class DrinkordersService(ABC):
    @abstractmethod
    def createDrinkorder(self, accountId, drinkorderItemList):
        pass
