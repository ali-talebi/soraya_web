from django.db import models
from django_jalali.db import models as django_jalali_models
from ckeditor.fields import RichTextField
from account.models import Profile
from django.urls import reverse

# Create your models here.



class Scheduleing(models.Model):
    name  = models.CharField(max_length=200 , verbose_name='نام زمان برگزاری به روز ( مثلا روز 1 ( چهارشنبه 1 بهمن )')
    guess = models.ForeignKey(Profile , on_delete=models.SET_NULL, null=True , verbose_name='فرد مهمان و سخنران' )
    time_start = models.CharField(verbose_name='زمان برگزاری' , max_length=10  )

    def __str__(self):
        return self.name




class Event_Information(models.Model):
    picture    = models.FileField(upload_to='Events/', verbose_name= 'تصویر رویداد' )
    event_name = models.CharField(max_length=100 , verbose_name="نام رویداد ")
    event_description = models.CharField(max_length= 500 , verbose_name="توضیح مختصر در خط ۱ ")
    creator = models.CharField(max_length=200 ,verbose_name='نام برگزار کننده')
    address = models.CharField(max_length=100 , verbose_name='آدرس')
    date    = django_jalali_models.jDateTimeField(verbose_name="زمان برگزاری")
    text    = RichTextField(verbose_name='متن رویداد')
    price   = models.BigIntegerField(verbose_name= 'میزان هزینه' )
    frame   = models.CharField(max_length=1000 , verbose_name='لوکیشن از روی نقشه ')
    guidance_1 = models.ForeignKey(Profile , on_delete=models.SET_NULL, null=True , verbose_name='فرد راهنمای شماره 1 ')
    guidance_2 = models.ForeignKey(Profile , related_name='guidance' , on_delete=models.SET_NULL, null=True , verbose_name='فرد راهنمای شماره 2 ')



    def get_absolute_url(self):
        return reverse('events:detail_event' , args=[str(self.id)])


    def __str__(self):
        return self.event_name


    class Meta :
        db_table = 'events_information'
        verbose_name_plural = 'رویداد های مدرسه '


