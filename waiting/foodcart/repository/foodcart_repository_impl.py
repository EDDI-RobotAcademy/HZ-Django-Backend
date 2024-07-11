from foodcart.entity.foodcart import Foodcart
from foodcart.repository.foodcart_repository import FoodcartRepository


class FoodcartRepositoryImpl(FoodcartRepository):
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

    def register(self, account):
        return Foodcart.objects.create(account=account)

    def findByAccount(self, account):
        try:
            return Foodcart.objects.get(account=account)
        except Foodcart.DoesNotExist:
            return None

    def findFoodcartIdByAccountId(self, accountId):
        foodcart = Foodcart.objects.get(account_id=accountId)
        return foodcart.foodcartId

