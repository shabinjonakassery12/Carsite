from django.db import models



class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name

    def get_car_count(self):
        return Cart1.objects.filter(car__brand=self).count()




class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    car_collection = models.CharField(max_length=30)

    def __str__(self):
        return self.car_collection



class Customer(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Cart1(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return  self.car.car_collection