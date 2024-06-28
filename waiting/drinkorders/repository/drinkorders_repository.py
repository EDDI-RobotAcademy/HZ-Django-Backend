from abc import ABC, abstractmethod


class DrinkordersRepository(ABC):
    @abstractmethod
    def create(self, accountId, status):
        pass
