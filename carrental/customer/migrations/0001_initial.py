# Generated by Django 4.1.2 on 2023-07-14 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('capacity', models.PositiveIntegerField(null=True)),
                ('color', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('un-available', 'un-available'), ('on-service', 'on-service')], default='available', max_length=25)),
                ('mileage', models.PositiveIntegerField(null=True)),
                ('fuel', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/cars/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('booked', 'booked'), ('confirmed', 'confirmed'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='booked', max_length=20)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.car')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/cars/')),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.car')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('amount', models.PositiveIntegerField(null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('whatsapp', models.CharField(max_length=20, null=True)),
                ('note', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id_proof', models.ImageField(null=True, upload_to='images/bookings/id_proofs/')),
                ('status', models.CharField(choices=[('booked', 'booked'), ('confirmed', 'confirmed'), ('in-progress', 'in-progress'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='booked', max_length=15)),
                ('reservations', models.ManyToManyField(to='customer.reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
