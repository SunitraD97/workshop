from django.contrib import admin
from .models import Cars , CAR_TYPES
# Register your models here.

admin.site.register(CAR_TYPES)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('carnumber','date','name','phone','car_type')
    search_fields = ('carnumber','car_type')

admin.site.register(Cars,CarsAdmin)
