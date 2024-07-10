from django.core.paginator import Paginator

from drinkorders.entity.drinkorders import Drinkorders
from foodorders.entity.foodorders import Foodorders
from purchase.entity.purchase import Purchase
from purchase.repository.purchase_repository import PurchaseRepository


class PurchaseRepositoryImpl(PurchaseRepository):
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

    def create(self, accountId):
        purchase = Purchase(account_id=accountId)

        # if foodorderId:
        #     try:
        #         foodorder = Foodorders.objects.get(id=foodorderId)
        #         purchase.foodorder = foodorder
        #     except Foodorders.DoesNotExist:
        #         raise ValueError(f"Foodorder with ID {foodorderId} does not exist.")
        #
        # if drinkorderId:
        #     try:
        #         drinkorder = Drinkorders.objects.get(id=drinkorderId)
        #         purchase.drinkorder = drinkorder
        #     except Drinkorders.DoesNotExist:
        #         raise ValueError(f"Drinkorder with ID {drinkorderId} does not exist.")

        purchase.save()
        return purchase

    def findById(self, purchaseId):
        try:
            purchase = Purchase.objects.select_related('account', 'foodorder', 'drinkorder').get(id=purchaseId)
            return purchase
        except Purchase.DoesNotExist:
            return None

    def findByAccountId(self, accountId):
        return Purchase.objects.filter(account_id=accountId)
