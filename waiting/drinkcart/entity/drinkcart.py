from django.db import models

from account.entity.account import Account


class Drinkcart(models.Model):
    drinkcartId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='drinkcarts')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Drinkcart -> id: {self.drinkcartId}, account: {self.account.id}"

    class Meta:
        db_table = 'drinkcart'
        app_label = 'drinkcart'

    def getAccount(self):
        return self.account
