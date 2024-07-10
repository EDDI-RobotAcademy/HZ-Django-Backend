from django.db import models

from drinkcart.entity.drinkcart import Drinkcart
from drink.entity.models import Drink


class DrinkcartItem(models.Model):
    drinkcartItemId = models.AutoField(primary_key=True)
    drinkcart = models.ForeignKey(Drinkcart, on_delete=models.CASCADE, related_name='items')
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    drinkquantity = models.PositiveIntegerField(default=1)
    drinkprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (f"DrinkcartItem -> id: {self.drinkcartItemId}, "
                f"drinkcart: {self.drinkcart.drinkcartId}, "
                f"drink: {self.drink.drinkName}, "
                f"drinkquantity: {self.drinkquantity}")

    class Meta:
        db_table = 'drinkcart_item'
        app_label = 'drinkcart'

    def getDrinkcart(self):
        return self.drinkcart
