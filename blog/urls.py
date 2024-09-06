from django.urls import path
from .views import DetailBlogView , TotalBlogsView

# Create your views here.



app_name = "blog"

urlpatterns = [
    path("total_blogs/" , TotalBlogsView.as_view() , name = "total_blog" ) ,
    path('detail_blog/<int:id>/' , DetailBlogView.as_view() , name="detail_blog" ) ,

]