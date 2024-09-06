from django.contrib import admin
from .models import Profile
from django.utils.html import format_html


# Register your models here.


@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
    list_display = ('person', 'name', 'family', 'status_person', 'gender', 'phone', 'show_img')
    list_editable = ('status_person',)

    def show_img(self, obj):
        if obj.picture:
            return format_html('<img  width=50px heigth=50px src="{}">'.format(obj.picture.url))
        else:
            return "بدون تصویر کاربری"

    show_img.short_description = 'تصویر کاربری'


