from foodorders.entity.foodorders_item import FoodordersItem
from foodorders.repository.foodorders_item_repository import FoodordersItemRepository
from food.entity.models import Food


class FoodordersItemRepositoryImpl(FoodordersItemRepository):
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

    def create(self, foodorders, food, foodprice, foodquantity):
        foodorder_item = FoodordersItem(foodorders=foodorders, food=food, foodprice=foodprice, foodquantity=foodquantity)
        foodorder_item.save()

