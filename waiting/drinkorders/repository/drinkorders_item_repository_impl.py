from drinkorders.entity.drinkorders_item import DrinkordersItem
from drinkorders.repository.drinkorders_item_repository import DrinkordersItemRepository
from drink.entity.models import Drink


class DrinkordersItemRepositoryImpl(DrinkordersItemRepository):
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

    def create(self, drinkorders, drink, drinkprice, drinkquantity):
        drinkorder_item = DrinkordersItem(drinkorders=drinkorders, drink=drink, drinkprice=drinkprice, drinkquantity=drinkquantity)
        drinkorder_item.save()

