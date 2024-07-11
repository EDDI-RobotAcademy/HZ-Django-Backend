from abc import ABC, abstractmethod


class FoodcartItemRepository(ABC):
    @abstractmethod
    def register(self, foodcartData, foodcart, food):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByFoodcart(self, foodcart):
        pass

    @abstractmethod
    def findByFoodId(self, foodId):
        pass

    @abstractmethod
    def findAllByFoodId(self, foodId):
        pass

    @abstractmethod
    def update(self, foodcartItem):
        pass

    @abstractmethod
    def deleteByFoodcartId(self, foodcartId):
        pass
