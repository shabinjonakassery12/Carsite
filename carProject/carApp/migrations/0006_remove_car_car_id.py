# Generated by Django 4.1.4 on 2022-12-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0005_cart1_car_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_id',
        ),
    ]
