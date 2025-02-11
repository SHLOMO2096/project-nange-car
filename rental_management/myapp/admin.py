from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Car, Customer, Rental

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Rental)
# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('brand', 'model', 'year', 'license_plate')  # הצגת מספר רישוי ברשימה
#     search_fields = ('license_plate',)  # אפשרות חיפוש לפי מספר רישוי