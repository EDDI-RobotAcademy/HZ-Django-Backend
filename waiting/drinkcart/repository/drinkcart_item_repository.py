from abc import ABC, abstractmethod


class DrinkcartItemRepository(ABC):
    @abstractmethod
    def register(self, drinkcartData, drinkcart, drink):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByDrinkcart(self, drinkcart):
        pass

    @abstractmethod
    def findByDrinkId(self, drinkId):
        pass

    @abstractmethod
    def findAllByDrinkId(self, drinkId):
        pass

    @abstractmethod
    def update(self, drinkcartItem):
        pass

    @abstractmethod
    def deleteByDrinkcartId(self, drinkcartId):
        pass
