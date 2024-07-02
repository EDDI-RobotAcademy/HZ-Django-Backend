from abc import ABC, abstractmethod


class DrinkordersRepository(ABC):
    @abstractmethod
    def create(self, accountId, status):
        pass

    @abstractmethod
    def findById(self, drinkorderId):
        pass
