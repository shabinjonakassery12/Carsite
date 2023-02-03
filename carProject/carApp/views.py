from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib import messages
from .models import Customer, Car, Cart1, Color, Brand
from django.db.models import Count, Sum
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage






def profile1(request):
    if 'id' in request.session:
        data2 = Car.objects.all()
        return render(request,'carsview.html',{'cars_list':data2})
    else:
        return redirect(customer_login_view)


def customer_login_view(request):
    if request.method == 'POST':
        username11 = request.POST['username1']
        password11 = request.POST['password1']
        data = Customer.objects.get(name=username11)
        if(data.password == password11):
            request.session['id'] = username11
            request.session['session_id'] = data.id
            return redirect(profile1)
        else:
            return HttpResponse('<script>{ alert("LOGIN FAILED") } </script>')
    else:
        return render(request,'customer_login.html')


def logout_view(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(customer_login_view)


def color_html_view(request):
    return render(request,'add_color_master.html')

def brand_html_view(request):
    return render(request,'add_brand_master.html')


def master_view(request):
    return render(request,'master.html')

def add_cars_view(request):
    id_b = Brand.objects.all()
    id_c = Color.objects.all()
    return render(request, 'add_cars.html', {'color_id':id_c, 'b_id':id_b})

def add_cus_view(request):
    return render(request,'add_cus.html')


def add_customer_master(request):
    if request.method == 'POST':
        username = request.POST['n1']
        password = request.POST['n2']
        data = Customer.objects.create(name=username,password=password)
        data.save()
        return HttpResponse('<script>{ alert("Added successfully") } </script>')



def add_cars_master(request):
    if request.method == 'POST':
        b_id = request.POST['brand_id']
        print(type(b_id))
        c_id = request.POST['color_id']
        print(c_id)
        car_series = request.POST['series']
        print(car_series)
        data = Car.objects.create(brand_id=b_id, color_id=c_id, car_collection=car_series)
        data.save()
        return HttpResponse('<script>{ alert("Added successfully") } </script>')

def add_color_view(request):
    if request.method == 'POST':
        color = request.POST['color']
        data = Color.objects.create(color_name=color)
    return HttpResponse('<script>{ alert("Added successfully") } </script>')

def add_brand_view(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        data = Brand.objects.create(brand_name=brand)
    return HttpResponse('<script>{ alert("Added successfully") } </script>')


def master_home_page(request):
    car_report = Cart1.objects.all().distinct('car')
    print(car_report)
    paginator = Paginator(car_report,3)
    page = request.GET.get('page')
    try:
        car_report = paginator.page(page)
    except PageNotAnInteger:
        car_report = paginator.page(1)
    except EmptyPage:
        car_report = paginator.page(paginator.num_pages)

    brand_report = Brand.objects.all().distinct('brand_name')
    print('car',Car.objects.filter(brand_id=1))
    return render(request,'master_home.html',{'c_report':car_report, 'b_report':brand_report, 'page':page})

def view_cart_car(request):
    data1 = Cart1.objects.filter(customer_id=request.session.get('session_id'))
    return render(request, 'cart_view.html', {'cart_list': data1})



def cart_added_view(request,id):
        car = Car.objects.get(id=id)
        print(car)
        customer = Customer.objects.get(id=request.session.get('session_id'))
        data1 = Cart1.objects.create(car=car, customer=customer)
        return HttpResponse('<script>{ alert("Added successfully") } </script>')



def remove_cart(request, id):
    item = Cart1.objects.filter(id=id)
    item.delete()
    messages.error(request, '   Cart is removed')
    return redirect(view_cart_car)