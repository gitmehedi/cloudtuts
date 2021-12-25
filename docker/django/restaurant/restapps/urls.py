from rest_framework import routers
from restapps import views
from django.urls import path,include,re_path
from .views import *

urlpatterns=[
    path('restaurant/', api_restaurant_list_view, name='restaurant-objects'),
    path('menu/', api_menu_list_view, name='menu-objects')
]