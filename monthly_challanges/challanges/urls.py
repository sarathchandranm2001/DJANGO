from django.urls import path
from.import views
urlpatterns = [ 
  path("<int:month>",views.monthly_ch_by_num) ,
  path("<str:month>",views.monthly_ch)
]