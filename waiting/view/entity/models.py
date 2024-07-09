from django.db import models

from account.entity.account import Account
from django.utils import timezone


class View(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='view')
    viewedMovie = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='viewedMovie')
    viewed_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"View {self.id} by {self.account}"

    class Meta:
        db_table = 'view'
        app_label = 'view'