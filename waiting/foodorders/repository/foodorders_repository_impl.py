from foodorders.entity.foodorders import Foodorders
from foodorders.repository.foodorders_repository import FoodordersRepository


class FoodordersRepositoryImpl(FoodordersRepository):
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

    def create(self, accountId, status):
        foodorders = Foodorders(account_id=accountId, status=status)
        foodorders.save()

        return foodorders

    def findById(self, foodorderId):
        return Foodorders.objects.get(id=foodorderId)
