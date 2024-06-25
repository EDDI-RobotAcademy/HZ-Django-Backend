from django.db import models

from account.entity.account import Account


class Foodcart(models.Model):
    foodcartId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='foodcarts')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foodcart -> id: {self.foodcartId}, account: {self.account.id}"

    class Meta:
        db_table = 'foodcart'
        app_label = 'foodcart'

    def getAccount(self):
        return self.account
