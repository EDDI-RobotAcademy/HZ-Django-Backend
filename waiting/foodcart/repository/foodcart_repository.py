from abc import ABC, abstractmethod


class FoodcartRepository(ABC):
    @abstractmethod
    def register(self, account):
        pass

    @abstractmethod
    def findByAccount(self, account):
        pass

    @abstractmethod
    def findFoodcartIdByAccountId(self, accountId):
        pass
