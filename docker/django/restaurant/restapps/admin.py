from django.contrib import admin

from .models import Restaurant, Menu


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'active')


admin.site.register(Restaurant, RestaurantAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'current_date', 'restaurant', 'active')


admin.site.register(Menu, MenuAdmin)
