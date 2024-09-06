from django.shortcuts import render
from django.views import View
from .models import Event_Information
# Create your views here.



class TotTalEventsView(View):

    template_name = ''

    def setup(self , request , *args , **kwargs ) :
        self.total_events =  Event_Information.objects.all()
        return super().setup(request , *args , **kwargs )


    def get(self ,request ) :
        return render(request, self.template_name , {} )





class DetailsView(View):
    template_name = 'events/event-detail.html'

    def setup(self , request , *args , **kwargs ) :
        self.event = Event_Information.objects.get(id = kwargs['id'])
        return super().setup(request , *args , **kwargs )


    def get(self ,request , id ) :
        return render(request , self.template_name , {'event' : self.event})



