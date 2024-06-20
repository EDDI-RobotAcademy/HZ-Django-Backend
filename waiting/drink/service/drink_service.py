from abc import abstractmethod, ABC

class DrinkService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createDrink(self, drinkName, drinkType, drinkDescription, drinkPrice, drinkImage ):
        pass

    @abstractmethod
    def readDrink(self, drinkId):
        pass

    @abstractmethod
    def removeDrink(self, drinkId):
        pass

    @abstractmethod
    def updateDrink(self, drinkId, drinkData):
        pass