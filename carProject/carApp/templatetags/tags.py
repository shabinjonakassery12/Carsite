from carApp.models import Cart1, Car, Brand
from django import template
from django.db.models import Count, Sum, Max, Avg, Min

register = template.Library()

@register.filter
def car_report(car_name):
    car_object = Car.objects.get(car_collection=car_name)
    car_report = Cart1.objects.filter(car=car_object).aggregate(count=Count('car')).get('count')
    return car_report

# @register.filter
# def brand_report(brand_name1):
#     print(brand_name1)
#     brand_objects = Car.objects.filter(brand=brand_name1)
#     brand_reports = Cart1.objects.filter(car=brand_objects).aggregate(count=Count('car')).get('count')
#     return brand_reports

