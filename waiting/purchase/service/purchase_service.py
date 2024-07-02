from abc import ABC, abstractmethod


class PurchaseService(ABC):
    @abstractmethod
    def createPurchase(self, accountId, foodorderId=None, drinkorderId=None):
        pass

    @abstractmethod
    def readPurchaseDetails(self, purchaseId, accountId):
        pass
