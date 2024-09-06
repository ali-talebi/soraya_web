from django.urls import path
from .views import TotTalEventsView , DetailsView


app_name = 'events'
urlpatterns = [
    path('total_events/', TotTalEventsView.as_view() , name='total_event') ,
    path('detailsEvent/<int:id>/', DetailsView.as_view(), name='detail_event' ) ,

]