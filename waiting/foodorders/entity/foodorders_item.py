from django.db import models

from foodorders.entity.foodorders import Foodorders
from food.entity.models import Food


class FoodordersItem(models.Model):
    id = models.AutoField(primary_key=True)
    foodorders = models.ForeignKey(Foodorders, related_name='foodorder_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodquantity = models.PositiveIntegerField(default=1)
    foodprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"FoodorderItem {self.id} for Foodorder {self.foodorders.id}"

    def total_price(self):
        return self.foodprice * self.foodquantity

    class Meta:
        db_table = 'foodorders_item'
        app_label = 'foodorders'