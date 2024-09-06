from django.shortcuts import render , redirect
from django.views import View
from .forms import LoginForm , SignUpForm , UpdateProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin
from country_city.models import City , Country

# Create your views here.





class ShowProfile(LoginRequiredMixin , View) :

    form_update   = UpdateProfileForm
    template_name = 'authenticate/instructor-edit-profile.html'


    def setup(self, request, *args, **kwargs):
        self.total_citys =  City.objects.all()
        self.total_country = Country.objects.all()
        self.client = request.user.person
        return super().setup(request , *args , **kwargs )
    
    def get(self ,request ) :
        return render(request , self.template_name , { 'total_city' : self.total_citys , 'total_country' : self.total_country , 'form':self.form_update(request.POST , instance= self.client )} )

    def post (self , request ) :
        form = self.form_update(request.POST , instance=request.user.person )
        try :
            picture = request.FILES['picture']
        except :
            picture = None

        if form.is_valid() :
            update_form_profile = form.save(commit=False)
            if picture is not None:
                update_form_profile.picture = picture
                update_form_profile.save()

            else :
                update_form_profile.save()

            messages.success(request , 'اطلاعات شما با موفقیت تغییر پیدا کرد' , 'success' )
            return redirect('home:home')
        else :
            messages.error(request , 'مشکلی در ثبت مشخصات شما وجود دارد' , 'error')

        return render(request , self.template_name , {'total_city' : self.total_citys , 'total_country' : self.total_country , 'form' : self.form_update(instance=  self.client  )})

class SignUpView(View):
    signup_form = SignUpForm
    template_name = 'authenticate/register.html'

    def get(self ,request ) :
        return render(request , self.template_name , {'form' : self.signup_form } )


    def post(self ,request ) :
        form = self.signup_form(request.POST)
        if form.is_valid() :

            n_email    = form.cleaned_data['email']
            n_password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            user_created = User.objects.create_user(username = n_email.split("@")[0] , email = n_email ,password = confirm_password )
            profile_created = Profile(person = user_created , phone =  '-' )
            profile_created.save()
            return redirect('home:home')
            messages.success ( request , 'با موفیت ثبت نام انجام شد' , 'success')

        else :
            messages.error ( request , 'مشكلي در ثبت نام به وجود آمده است' , 'error')


        return render(request , self.template_name , {'form' : self.signup_form } )

class LoginView(View):




    login_form = LoginForm
    template_name = 'authenticate/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')

        return super().dispatch(request, *args, **kwargs)

    def get(self ,request ):
        return render(request, self.template_name , {'form' : self.login_form} )


    def post(self  ,request ):
        form = self.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password )
            if user :
                login(request , user )
                messages.success(request, f'{request.user.username} با موفقیت وارد شدید'  , 'success')
                return redirect('home:home')

            else :
                messages.error(request , 'مشکلی در ورود دارید' , 'error')



        return render(request, self.template_name , {'form' : self.login_form} )



class LogoutView(LoginRequiredMixin , View) :

    def get(self , request ):
        messages.success(request, f'با موفقیت خارج شدید {request.user.username}', 'success')
        logout(request)

        return redirect('home:home')