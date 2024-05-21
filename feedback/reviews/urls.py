from django.urls import path
from .import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),#class based views implimentation
    path('thank-you',views.ThankYouView.as_view())
]
