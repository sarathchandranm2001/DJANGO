from django.urls import path
from.import views
urlpatterns = [ 
    path("january",views.jan),
    path("february",views.feb),
     path("<month>",views.monthly_ch)
]