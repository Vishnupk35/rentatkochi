# Generated by Django 4.1.2 on 2023-07-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('manual', 'manual'), ('automatic', 'automatic')], max_length=25, null=True),
        ),
    ]
