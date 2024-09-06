from django.urls import path
from .views import LoginView, SignUpView, LogoutView , ShowProfile

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('showprofile/', ShowProfile.as_view(), name='show_profile') ,

]