from django.contrib import admin
from .models import Event_Information
# Register your models here.



@admin.register(Event_Information)
class Event_Information_Admin(admin.ModelAdmin):
    list_display = ('event_name' , 'date' , 'price' , 'creator' )

