from django.db import models
from food.entity.models import Food
from .foodorder import Foodorder

class FoodorderItem(models.Model):
    foodorder_item_id = models.AutoField(primary_key=True)
    foodorder = models.ForeignKey(Foodorder, related_name='foodorder_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"FoodorderItem {self.foodorder_item_id} for Foodorder {self.foodorder.foodorder_id}"

    class Meta:
        db_table = 'foodorder_item'
        app_label = 'food_order'