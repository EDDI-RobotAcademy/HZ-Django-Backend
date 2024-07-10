from purchase.entity.purchase_item import PurchaseItem
from purchase.repository.purchase_item_repository import PurchaseItemRepository
from food.entity.models import Food
from drink.entity.models import Drink


class PurchaseItemRepositoryImpl(PurchaseItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, purchase, food, foodprice, foodquantity, drink, drinkprice, drinkquantity):
        purchase_item = PurchaseItem(purchase=purchase, food=food, foodprice=foodprice, foodquantity=foodquantity,
                                     drink=drink, drinkprice=drinkprice, drinkquantity=drinkquantity)
        purchase_item.save()

    def findAllByPurchase(self, purchase):
        return PurchaseItem.objects.filter(purchase=purchase)

    def findAllByPurchaseList(self, purchaseList):
        return PurchaseItem.objects.filter(purchase__in=purchaseList)
