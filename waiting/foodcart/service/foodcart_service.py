from abc import ABC, abstractmethod


class FoodcartService(ABC):
    @abstractmethod
    def foodcartRegister(self, foodcartData, accountId):
        pass

    @abstractmethod
    def foodcartList(self, accountId):
        pass

    @abstractmethod
    def removeFoodcartItem(self, accountId):
        pass