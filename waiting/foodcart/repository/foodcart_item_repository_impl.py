from foodcart.entity.foodcart import Foodcart
from foodcart.entity.foodcart_item import FoodcartItem
from foodcart.repository.foodcart_item_repository import FoodcartItemRepository


class FoodcartItemRepositoryImpl(FoodcartItemRepository):
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

    def register(self, foodcartData, foodcart, food):
        foodPrice = foodcartData.get('foodPrice')
        foodquantity = foodcartData.get('foodquantity')

        FoodcartItem.objects.create(
            foodcart=foodcart,
            food=food,
            foodquantity=foodquantity,
            foodprice=foodPrice
        )

    def findById(self, id):
        return FoodcartItem.objects.get(foodcartItemId=id)

    def findByFoodcart(self, foodcart):
        return list(FoodcartItem.objects.filter(foodcart=foodcart))

    def findByFoodId(self, foodId):
        try:
            return FoodcartItem.objects.get(food_id=foodId)
        except FoodcartItem.DoesNotExist:
            return None

    def findAllByFoodId(self, foodId):
        return FoodcartItem.objects.filter(food_id=foodId)

    def update(self, foodcartItem):
        foodcartItem.save()

    def deleteByFoodcartId(self, foodcartId):
        foodcartitem = FoodcartItem.objects.filter(foodcart_id=foodcartId)
        foodcartitem.delete()
