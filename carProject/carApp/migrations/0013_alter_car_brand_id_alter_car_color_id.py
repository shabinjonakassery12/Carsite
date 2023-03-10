# Generated by Django 4.1.4 on 2022-12-09 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0012_brand_color_remove_car_car_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carApp.brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carApp.color'),
        ),
    ]
