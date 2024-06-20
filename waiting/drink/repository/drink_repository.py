from abc import abstractmethod, ABC

class DrinkRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, drinkName, drinkType, drinkDescription, drinkPrice, drinkImage):
        pass

    @abstractmethod
    def findByDrinkId(self, drinkId):
        pass

    @abstractmethod
    def deleteByDrinkId(self, drinkId):
        pass

    @abstractmethod
    def update(self, drink, drinkData):
        pass
