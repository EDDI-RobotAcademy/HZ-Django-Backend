from abc import abstractmethod, ABC

class FoodRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, foodName, foodType, foodDescription, foodPrice, foodImage):
        pass

    @abstractmethod
    def findByFoodId(self, foodId):
        pass

    @abstractmethod
    def deleteByFoodId(self, foodId):
        pass

    @abstractmethod
    def update(self, food, foodData):
        pass
