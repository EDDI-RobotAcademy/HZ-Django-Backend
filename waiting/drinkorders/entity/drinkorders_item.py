from django.db import models

from drinkorders.entity.drinkorders import Drinkorders
from drink.entity.models import Drink


class DrinkordersItem(models.Model):
    id = models.AutoField(primary_key=True)
    drinkorders = models.ForeignKey(Drinkorders, related_name='drinkorder_items', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DrinkorderItem {self.id} for Drinkorder {self.drinkorders.id}"

    def total_price(self):
        return self.price * self.quantity

    class Meta:
        db_table = 'drinkorders_item'
        app_label = 'drinkorders'