from django.db import models

from purchase.entity.purchase import Purchase
from food.entity.models import Food
from drink.entity.models import Drink


class PurchaseItem(models.Model):
    id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, related_name='purchase_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodquantity = models.PositiveIntegerField(default=1)
    foodprice = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    drinkquantity = models.PositiveIntegerField(default=1)
    drinkprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PurchaseItem {self.id} for Purchase {self.purchase.id}"

    def total_price(self):
        return self.foodprice * self.foodquantity + self.drinkprice * self.drinkquantity

    class Meta:
        db_table = 'purchase_item'
        app_label = 'purchase'