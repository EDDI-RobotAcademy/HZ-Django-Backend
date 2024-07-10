from abc import ABC, abstractmethod


class PurchaseRepository(ABC):
    @abstractmethod
    def create(self, accountId):
        pass

    @abstractmethod
    def findById(self, purchaseId):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass
