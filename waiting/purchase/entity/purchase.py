from django.db import models

from account.entity.account import Account
from django.utils import timezone

from drinkorders.entity.drinkorders import Drinkorders
from foodorders.entity.foodorders import Foodorders


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='purchase')
    foodorder = models.ForeignKey(Foodorders, on_delete=models.CASCADE,
                                  null=True, blank=True, related_name='purchase')
    drinkorder = models.ForeignKey(Drinkorders, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='purchase')
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchase {self.id} - Account: {self.account}, Foodorder: {self.foodorder}, Drinkorder: {self.drinkorder}"

    class Meta:
        db_table = 'purchase'
        app_label = 'purchase'