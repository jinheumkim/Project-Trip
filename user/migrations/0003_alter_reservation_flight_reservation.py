# Generated by Django 4.2.7 on 2024-04-10 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_flightprice_price'),
        ('user', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight_reservation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='FlightSchedule', to='flight.flightschedule'),
        ),
    ]
