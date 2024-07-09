from django.db import models

from account.entity.account import Account
from subscription.entity.models import Subscription


class SubscriptionManage(models.Model):
    subscriptionManageId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    startDate = models.DateTimeField(null=False)
    endDate = models.DateTimeField(null=False)
    subscriptionManageRegisteredDate = models.DateTimeField(auto_now_add=True)
    subscriptionManageUpdatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.account} - {self.subscription}'

    class Meta:
        db_table = 'subscription_manage'