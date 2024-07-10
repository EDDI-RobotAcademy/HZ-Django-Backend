from abc import ABC, abstractmethod


class PurchaseItemRepository(ABC):
    @abstractmethod
    def create(self, purchase, food, foodprice, foodquantity, drink, drinkprice, drinkquantity):
        pass

    @abstractmethod
    def findAllByPurchase(self, purchase):
        pass

    @abstractmethod
    def findAllByPurchaseList(self, purchaseList):
        pass
