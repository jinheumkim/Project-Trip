# Generated by Django 4.2.7 on 2024-04-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_alter_flightprice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
    ]