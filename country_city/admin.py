from django.contrib import admin
from .models import City, Country


# Register your models here.


@admin.register(City)
class City_Admin(admin.ModelAdmin):
    list_display = ('name_city', 'main_country')
    list_editable = ('main_country',)


@admin.register(Country)
class Country_Admin(admin.ModelAdmin):
    list_display = ('country_name',)