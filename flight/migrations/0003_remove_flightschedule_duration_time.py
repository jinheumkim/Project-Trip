# Generated by Django 4.2.7 on 2024-03-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_alter_flightschedule_arrival_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightschedule',
            name='duration_time',
        ),
    ]