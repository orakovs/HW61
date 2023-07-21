from django.shortcuts import render
from .models import *


def homeView(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.get(user=user)

        context = {'Customer': customer,
                   'Message': 'Привет, меня зовут'}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
