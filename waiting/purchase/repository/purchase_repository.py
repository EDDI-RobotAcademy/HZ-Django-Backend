from abc import ABC, abstractmethod


class PurchaseRepository(ABC):
    @abstractmethod
    def create(self, accountId, foodorderId=None, drinkorderId=None):
        pass

    @abstractmethod
    def findById(self, purchaseId):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass
