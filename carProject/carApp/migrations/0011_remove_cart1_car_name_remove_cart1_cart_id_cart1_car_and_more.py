# Generated by Django 4.1.4 on 2022-12-09 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0010_remove_cart1_car_id_cart1_car_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart1',
            name='car_name',
        ),
        migrations.RemoveField(
            model_name='cart1',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='cart1',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carApp.car'),
        ),
        migrations.AddField(
            model_name='cart1',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carApp.customer'),
        ),
    ]
