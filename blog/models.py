from django.db import models
from ckeditor.fields import  RichTextField
from account.models import Profile
from django_jalali.db import models as jmodels
from account.models import Profile
from django.urls import reverse
# Create your models here.



class Category_Blog(models.Model) :
    name = models.CharField(verbose_name = 'نام دسته بندی' , max_length=100  , unique = True )
    slug = models.SlugField(verbose_name = 'آدرس دسته بندی'  )


    def __str__(self ) :
        return self.name



    class Meta :
        db_table = 'Category_Blog'
        verbose_name_plural = 'دسته بندی های وبلاگ'



class Tags_Post(models.Model) :
    name = models.CharField(verbose_name = 'نام تگ' , max_length = 100 )

    def __str__(self ) :
        return self.name

    class Meta :
        db_table = 'Tags_Post'
        verbose_name_plural  = 'تگ های پست ها'


class Post(models.Model) :

    summer_text = RichTextField(verbose_name = 'خلاصه متن' , null = True  )
    author  = models.ForeignKey(Profile , verbose_name = 'نویسنده'  ,    on_delete = models.CASCADE ,  null = True   )
    picture = models.FileField(verbose_name = 'تصویر' , upload_to = 'blog/Post/' )
    name = models.CharField(max_length   = 100 , verbose_name = 'عنوان پست' )
    slug = models.SlugField(verbose_name = 'آدرس اینترنتی' )
    category     = models.ForeignKey(Category_Blog , on_delete = models.CASCADE , related_name = 'post' , verbose_name = 'دسته بندی ' )
    description1 = RichTextField(verbose_name = 'توضیحات' , blank = True )
    description2 = RichTextField(verbose_name = 'توضیحات' , blank = True , null = True  )
    tags  = models.ManyToManyField(Tags_Post , verbose_name = 'تگ ها'  )
    times = jmodels.jDateTimeField(auto_now_add = True , verbose_name = 'زمان ایجاد'   ,  null = True )
    time_to_read = models.PositiveIntegerField(verbose_name = 'زمان  خواندن' , null = True )
    author_idea  = RichTextField(verbose_name = 'نظر نویسنده', null = True  )
    banner1      = models.FileField(verbose_name = 'بنر تبلیغاتی 1 '  , upload_to = "Post/Banner/banner1" , null = True  )
    banner2      = models.FileField(verbose_name = 'بنر تبلیغاتی 2 '  , upload_to = "Post/Banner/banner2" , null = True  )
    banner3      = models.FileField(verbose_name = 'بنر تبلیغاتی  3'  , upload_to = "Post/Banner/banner3" , null = True  )



    def __str__(self) :
        return self.name




    def get_absolute_url(self) :
        return reverse('blog:detail_blog' , args = [str(self.id)])


    class Meta :
        db_table = 'Post'
        verbose_name_plural = 'پست های وبلاگ'
        ordering = ['times']






class PostComment(models.Model) :

    STATUS_POST_COMMENT = (
        ('no_check' , 'بدون چک' ) ,
        ('checheck' , 'چک' ) ,
        ('pass'     , 'تایید' )
        )
    post_selected  = models.ForeignKey(Post , verbose_name = 'پست انتخاب شده'  , null = True ,on_delete = models.CASCADE  )
    name    = models.CharField(verbose_name  = 'نام پاسخ دهنده'    , max_length = 100  )
    email   = models.EmailField(verbose_name = 'ایمیل پاسخ دهنده'  )
    text    = models.TextField(verbose_name  = 'متن پاسخ'   )
    status  = models.CharField(max_length    = 20 , choices = STATUS_POST_COMMENT , default = 'no_check' , verbose_name = 'وضعیت بررسی کامنت' )
    times   = jmodels.jDateTimeField(verbose_name = '' , null = True , auto_now_add = True )
    def __str__(self) :
        return self.name

    class Meta :
        db_table = 'PostComment'
        verbose_name_plural = 'کامنت های وبلاگ'