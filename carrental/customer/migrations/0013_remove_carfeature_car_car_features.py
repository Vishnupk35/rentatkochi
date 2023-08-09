# Generated by Django 4.1.2 on 2023-08-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_booking_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carfeature',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.ManyToManyField(to='customer.carfeature'),
        ),
    ]