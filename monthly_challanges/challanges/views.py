from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def jan(request):
    return HttpResponse("jan")
def feb(request):
    return HttpResponse("feb")

