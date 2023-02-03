"""carProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from carApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile1),
    path('customer_login', views.customer_login_view),
    path('logout', views.logout_view),
    path('master/', views.master_view),
    path('customer_html', views.add_cus_view, name="customer_view"),
    path('cars_html', views.add_cars_view, name="cars_view"),
    path('color_html', views.color_html_view, name="color_view"),
    path('brand_html', views.brand_html_view, name="brand_view"),
    path('add_cust', views.add_customer_master),
    path('add_cars', views.add_cars_master),
    path('add_color', views.add_color_view),
    path('add_brand', views.add_brand_view),
    path('view_cart', views.view_cart_car, name="cart_view"),
    path('add/<int:id>', views.cart_added_view),
    path('remove/<int:id>', views.remove_cart, name="delete"),
    path('master_home_page',views.master_home_page,name="master_home_page")
]
