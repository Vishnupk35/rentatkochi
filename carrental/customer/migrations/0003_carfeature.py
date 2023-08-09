# Generated by Django 4.1.2 on 2023-07-14 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_car_transmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.car')),
            ],
        ),
    ]
