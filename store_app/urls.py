from django.urls import path
from .views import *

urlpatterns = [
    path('home', homeView, name='home_url'),
    path('get_goods_by_category/<int:pk>', getGoodsByCategory, name='goods_by_category_url'),
    path('get_plants_by_type/<int:pk>', getPlantByType, name='plants_by_type_url')
]
