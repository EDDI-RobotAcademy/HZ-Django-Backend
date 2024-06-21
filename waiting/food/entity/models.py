from django.db import models

# Create your models here.
class Food(models.Model):
    foodId = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=128, null=False)
    foodType = models.CharField(max_length=128, null=False)
    foodDescription = models.TextField()
    foodPrice = models.DecimalField(max_digits=10, decimal_places=2)
    foodImage = models.CharField(max_length=100, null=True)

    foodRegisteredDate = models.DateTimeField(auto_now_add=True)
    foodUpdatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'food'
