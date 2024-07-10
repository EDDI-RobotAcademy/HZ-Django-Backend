from abc import ABC, abstractmethod


class PurchaseService(ABC):
    @abstractmethod
    def createPurchase(self, accountId, purchaseItemList):
        pass

    @abstractmethod
    def readPurchaseDetails(self, purchaseId, accountId):
        pass
