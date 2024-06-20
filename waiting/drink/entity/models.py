from django.db import models

# Create your models here.
class Drink(models.Model):
    drinkId = models.AutoField(primary_key=True)
    drinkName = models.CharField(max_length=128, null=False)
    drinkType = models.CharField(max_length=128, null=False)
    drinkDescription = models.TextField()
    drinkPrice = models.DecimalField(max_digits=10, decimal_places=2)
    drinkImage = models.CharField(max_length=100, null=True)

    drinkRegisteredDate = models.DateTimeField(auto_now_add=True)
    drinkUpdatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'drink'
