# Generated by Django 5.0.6 on 2024-07-10 05:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("drinkcart", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drinkcartitem",
            old_name="price",
            new_name="drinkprice",
        ),
        migrations.RenameField(
            model_name="drinkcartitem",
            old_name="quantity",
            new_name="drinkquantity",
        ),
    ]
