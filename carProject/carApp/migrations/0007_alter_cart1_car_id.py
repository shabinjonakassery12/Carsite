# Generated by Django 4.1.4 on 2022-12-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0006_remove_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart1',
            name='car_id',
            field=models.CharField(max_length=200),
        ),
    ]