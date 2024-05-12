from django.urls import path
from.import views
urlpatterns = [ 
  path("",views.index,name="index"),#/challanges/nothing will be triggered  
  path("<int:month>",views.monthly_ch_by_num) ,
  path("<str:month>",views.monthly_ch,name="month-challenge")
]