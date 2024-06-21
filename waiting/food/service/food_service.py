from abc import abstractmethod, ABC

class FoodService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createFood(self, foodName, foodType, foodDescription, foodPrice, foodImage ):
        pass

    @abstractmethod
    def readFood(self, foodId):
        pass

    @abstractmethod
    def removeFood(self, foodId):
        pass

    @abstractmethod
    def updateFood(self, foodId, foodData):
        pass