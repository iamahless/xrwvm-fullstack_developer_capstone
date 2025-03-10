from django.contrib import admin
from .models import CarMake, CarModel


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country']


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'year', 'car_make', 'dealer_id']
    list_filter = ['type', 'year', 'car_make']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
