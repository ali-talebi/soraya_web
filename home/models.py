from django.db import models
from ckeditor.fields import RichTextField
from account.models import Profile


# Create your models here.









class MainSlider(models.Model):
    name = models.CharField(verbose_name="نام تصویر", max_length=100)
    text = models.CharField(verbose_name= "متن صفحه اول" , max_length= 100 , null = True )
    picture = models.FileField(verbose_name='تصویر', upload_to='MainSlider/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MainSlider'
        verbose_name_plural = 'تصاویر اسلایدر ابتدایی'


class AboutUs(models.Model):
    text_goad = models.CharField(verbose_name='متن هدف در درباره ما', max_length=50, null=True)
    picture1 = models.FileField(verbose_name='تصویر 1 ', null=True)
    picture2 = models.FileField(verbose_name='تصویر 2 ', null=True)
    picture3 = models.FileField(verbose_name='تصویر 3 ', null=True)
    picture4 = models.FileField(verbose_name='تصویر 4 ', null=True)

    title = models.CharField(max_length=100, verbose_name='درباره ما')
    picture = models.FileField(upload_to='AboutUs/', verbose_name='تصویر درباره ما')

    title_1 = models.CharField(max_length=100, verbose_name='توضیحات 1 ', null=True)
    text1 = RichTextField(verbose_name='توضیحات 1', null=True, blank=True)
    title_2 = models.CharField(max_length=100, verbose_name='توضیحات 2 ', null=True)
    text2 = RichTextField(verbose_name='توضیحات 2', null=True, blank=True)

    title_3 = models.CharField(max_length=100, verbose_name='توضیحات 3 ', null=True)
    text3 = RichTextField(verbose_name='توضیحات 3 ', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'AboutUs'
        verbose_name_plural = 'درباره ما'
        ####


class FAQ(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان سوال')
    text = RichTextField(verbose_name='متن')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'FAQ'
        verbose_name_plural = 'سوالات پر تکرار '


class ContactUs(models.Model):
    STATUS_CHOICES = (
        ('pre', 'بدون بررسی'), ('now', 'در حال بررسی'), ('end', 'تمام شده')
    )

    name = models.CharField(verbose_name="نام", max_length=100)
    family = models.CharField(verbose_name="نام خانوادگی", max_length=100)
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(verbose_name='شماره تلفن', max_length=11, null=True)
    text = models.TextField(verbose_name="متن")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pre')

    def __str__(self):
        return f'{self.name} - {self.family} '

    class Meta:
        db_table = "ContactUs"
        verbose_name_plural = 'ارتباط با ما'


class Supporter(models.Model):
    name = models.CharField(verbose_name='نام حامی ما', max_length=100)
    picture = models.FileField(verbose_name='لوگو', upload_to='Supporter/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Supporter'
        verbose_name_plural = 'همراهان ما'


class MyTeams(models.Model):
    picture = models.FileField(upload_to="MyTeams/Picture/", verbose_name='تصویر هم تیمی')
    position = models.CharField(max_length=100, verbose_name='سمت در شرکت', null=True)
    full_name = models.CharField(verbose_name='نام و نام خانوادگی', max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'MyTeams'
        verbose_name_plural = 'هم تیمی ها'


class Year_Student_Stuff(models.Model):
    year = models.CharField(verbose_name='سال', max_length=5)
    text = models.CharField(verbose_name= 'متن ورودی' , max_length = 50 , null = True )

    def __str__(self):
        return self.year

    class Meta:
        db_table = 'Year_Student_Stuff'
        verbose_name_plural = 'تعداد دانش آموزان و کارمندان در سال '

