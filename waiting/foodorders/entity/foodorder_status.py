from django.db import models


class FoodorderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'
