from drinkcart.entity.drinkcart import Drinkcart
from drinkcart.entity.drinkcart_item import DrinkcartItem
from drinkcart.repository.drinkcart_item_repository import DrinkcartItemRepository


class DrinkcartItemRepositoryImpl(DrinkcartItemRepository):
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

    def register(self, drinkcartData, drinkcart, drink):
        drinkPrice = drinkcartData.get('drinkPrice')
        drinkquantity = drinkcartData.get('drinkquantity')

        DrinkcartItem.objects.create(
            drinkcart=drinkcart,
            drink=drink,
            drinkquantity=drinkquantity,
            drinkprice=drinkPrice
        )

    def findById(self, id):
        return DrinkcartItem.objects.get(drinkcartItemId=id)

    def findByDrinkcart(self, drinkcart):
        return list(DrinkcartItem.objects.filter(drinkcart=drinkcart))

    def findByDrinkId(self, drinkId):
        try:
            return DrinkcartItem.objects.get(drink_id=drinkId)
        except DrinkcartItem.DoesNotExist:
            return None

    def findAllByDrinkId(self, drinkId):
        return DrinkcartItem.objects.filter(drink_id=drinkId)

    def update(self, drinkcartItem):
        drinkcartItem.save()

    def deleteByDrinkcartId(self, drinkcartId):
        drinkcartitem = DrinkcartItem.objects.filter(drinkcart_id=drinkcartId)
        drinkcartitem.delete()


