from django.shortcuts import render
from .models import *


def homeView(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.get(user=user)

        categories = Category.objects.all()
        types = Type.objects.all()
        context = {'Customer': customer,
                   'Message': 'Привет, меня зовут',
                   'Categories': categories,
                   'Types': types}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def getGoodsByCategory(request, pk):
    goods = Good.objects.filter(category=pk)
    context = {'goods': goods}
    return render(request, 'goods_by_category.html', context)


def getPlantByType(request, pk):
    plants = Plant.objects.filter(type=pk)
    context = {'plants': plants}
    return render(request, 'plants_by_type.html', context)
