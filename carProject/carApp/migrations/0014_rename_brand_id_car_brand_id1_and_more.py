# Generated by Django 4.1.4 on 2022-12-12 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0013_alter_car_brand_id_alter_car_color_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='brand_id',
            new_name='brand_id1',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='color_id',
            new_name='color_id2',
        ),
    ]
