from django.db import models


class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscriptionName = models.CharField(max_length=128, null=False)
    subscriptionType = models.CharField(max_length=128, null=False)
    subscriptionPrice = models.DecimalField(max_digits=10, decimal_places=2)
    subscriptionRegisteredDate = models.DateTimeField(auto_now_add=True)
    subscriptionUpdatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriptionName

    class Meta:
        db_table = 'subscription'