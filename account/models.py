from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from country_city.models import Country, City


# Create your models here.


class Profile(models.Model):
    GENDER_STATUS = (('---', 'نامشخص'), ('man', 'آقا'), ('female', 'خانم'))
    STATUS_PERSON_LEVEL = (('school_student', 'دانش آموز'), ('uni_student', 'دانشجو'), ('interest', 'علاقه مند'))



    person = models.OneToOneField(User , related_name='person' ,  verbose_name='فرد مورد نظر', on_delete=models.SET_NULL, null=True )

    name   = models.CharField(max_length=100, verbose_name='نام' , null = True )

    family = models.CharField(max_length=100, verbose_name='نام خانوادگی', null = True )
    father_name = models.CharField(verbose_name='نام پدر', max_length=20, null = True )
    unique_code = models.CharField(max_length=30, verbose_name='کد ملی یا اتباع',
                                   help_text='لطفا کد ملی یا اتباع را وراد نمایید',null = True)
    happy_birthday = models.DateTimeField(verbose_name='تاریخ تولد',
                                          help_text='در نظر داشته باشید افراد خارجی تاریخ تولد چطور ثبت شود',
                                          null = True)
    country = models.OneToOneField(Country, verbose_name='نام کشور', on_delete=models.SET_NULL, null=True)
    city = models.OneToOneField(City, verbose_name='نام شهر', on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن', null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name='جنسیت', choices=GENDER_STATUS, default='---' )
    picture = models.FileField(upload_to='Profile/Picture/', verbose_name='تصویر کاربری', null=True, blank=True)
    additaion_address = models.TextField(verbose_name='جزئیات آدرس', null=True, blank=True, default='--')
    status_person = models.CharField(max_length=40, verbose_name='وضعیت فرد مورد نظر', null=True, blank=True , choices=STATUS_PERSON_LEVEL, default='interest')


    def __str__(self):
        return f' {self.name} - {self.family}'


    class Meta:
        db_table = 'Profile_Information'
        verbose_name_plural = 'اطلاعات حساب کاربری'
