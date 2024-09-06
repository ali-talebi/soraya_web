from django.db import models


# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50, verbose_name='نام کشور')

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = 'Country'
        verbose_name_plural = 'نام کشور های موجود'


class City(models.Model):
    main_country = models.OneToOneField(Country, related_name='main_country', verbose_name='نام کشور ',
                                        on_delete=models.SET_NULL, null=True)
    name_city = models.CharField(max_length=100, verbose_name='نام شهر')

    def __str__(self):
        return self.name_city

    class Meta:
        db_table = 'City'
        verbose_name_plural = 'نام شهر هاي موجود'