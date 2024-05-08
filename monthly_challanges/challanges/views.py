from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def jan(request):
    return HttpResponse("jan")
def feb(request):
    return HttpResponse("feb")
def monthly_ch(request,month):
    if month == 'mar':
        return HttpResponse("mar")
    elif month == 'apr':
        return HttpResponse("apr")
    else:
        return HttpResponse("no month")

