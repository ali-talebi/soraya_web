from django.shortcuts import render, redirect
from django.views import View
from .models import AboutUs, FAQ, ContactUs, Supporter, MainSlider, MyTeams, Year_Student_Stuff
from django.contrib import messages
from .forms import ContactUsForm
from blog.models import Post
from events.models import Event_Information

# Create your views here.


class HomeView(View):
    template_name = 'home/index-5.html'

    def setup(self, request, *args, **kwargs):
        self.supporter = Supporter.objects.all()

        self.blog1  = Post.objects.all()[0]
        self.blog2 = Post.objects.all()[1]
        self.blog3 = Post.objects.all()[2]
        self.blog4 = Post.objects.all()[3]
        self.events = Event_Information.objects.all()
        self.picture_slider = MainSlider.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, { 'events':self.events ,  'blog4':self.blog4  , 'blog3':self.blog3  , 'blog2':self.blog2  ,  'blog1':self.blog1  , 'supporter': self.supporter, 'picture_slider': self.picture_slider})

    def post(self, request):
        return render(request, self.template_name, { 'events':self.events , 'blog1':self.blog1  , 'supporter': self.supporter, 'picture_slider': self.picture_slider})


class AboutUserView(View):
    template_name = 'home/about.html'

    def setup(self, request, *args, **kwargs):
        self.data = AboutUs.objects.first()
        self.my_team = MyTeams.objects.all()
        self.partners = Supporter.objects.all()
        self.info_company_stuff_student = Year_Student_Stuff.objects.all()

        return super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name,
                      {'data': self.data, 'my_teams': self.my_team, 'partners': self.partners,
                       'info': self.info_company_stuff_student})


class FAQView(View):
    template_name = 'home/faq.html'

    def setup(self, request, *args, **kwargs):
        self.data = FAQ.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'data': self.data})


class ContactUsView(View):
    contact_us_form = ContactUsForm
    template_name = 'home/contact-us.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        form = self.contact_us_form(request.POST)
        if form.is_valid():
            new_contact_us = form.save()
            return redirect('home:home')

        return render(request, self.template_name, {'form': self.contact_us_form()})









def custom_404(request, exception):
    return render(request, 'home/error-404.html', status=404)







