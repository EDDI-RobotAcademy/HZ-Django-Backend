from django.db import models
from drink.entity.models import Drink
from .drinkorder import Drinkorder

class DrinkorderItem(models.Model):
    drinkorder_item_id = models.AutoField(primary_key=True)
    drinkorder = models.ForeignKey(Drinkorder, related_name='drinkorder_items', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DrinkorderItem {self.drinkorder_item_id} for Drinkorder {self.drinkorder.drinkorder_id}"

    class Meta:
        db_table = 'drinkorder_item'
        app_label = 'drink_order'