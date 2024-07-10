from django.db import models

from foodcart.entity.foodcart import Foodcart
from food.entity.models import Food


class FoodcartItem(models.Model):
    foodcartItemId = models.AutoField(primary_key=True)
    foodcart = models.ForeignKey(Foodcart, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodquantity = models.PositiveIntegerField(default=1)
    foodprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (f"FoodcartItem -> id: {self.foodcartItemId}, "
                f"foodcart: {self.foodcart.foodcartId}, "
                f"food: {self.food.foodName}, "
                f"foodquantity: {self.foodquantity}")

    class Meta:
        db_table = 'foodcart_item'
        app_label = 'foodcart'

    def getFoodcart(self):
        return self.foodcart
