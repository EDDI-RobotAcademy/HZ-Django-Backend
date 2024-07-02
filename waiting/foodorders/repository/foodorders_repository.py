from abc import ABC, abstractmethod


class FoodordersRepository(ABC):
    @abstractmethod
    def create(self, accountId, status):
        pass

    @abstractmethod
    def findById(self, foodorderId):
        pass
