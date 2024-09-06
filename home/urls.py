from django.urls import path
from .views import HomeView , AboutUserView , FAQView  , ContactUsView


app_name = 'home'


urlpatterns = [

    path('' , HomeView.as_view() , name = 'home' ) ,
    path('aboutus/' , AboutUserView.as_view() , name = 'aboutus' ) ,
    path('faq/' , FAQView.as_view() , name="faq" ) ,
    path('contactus/' , ContactUsView.as_view() , name='contactus' ) ,

]