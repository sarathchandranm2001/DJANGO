from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
monthly_cha = {
    "january": "Read books",
    "february": "Learn a new skill",
    "march": "Start a daily journal",
    "april": "Practice mindfulness",
    "may": "Start a fitness routine",
    "june": "Explore outdoor activities",
    "july": "Volunteer in your community",
    "august": "Try a new hobby",
    "september": "Set personal goals",
    "october": "Learn a new recipe each week",
    "november": "Practice gratitude daily",
    "december": "Give back to those in need"
}

def index(request):
    list_items = ""
    months = list(monthly_cha.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return render(request,"challanges/index.html",{"months":months})

# Create your views here.
def monthly_ch_by_num(request, month):
    months = list(monthly_cha.keys())
    if 1 <= month <= len(months):
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invalid month number")

def monthly_ch(request, month):
    try:
        challenge_text = monthly_cha[month]
       
        return render(request,'challanges/challange.html',{"text":challenge_text ,
                                                           "month_name":month.capitalize()
                                                           })
    except KeyError:
       response_data= render_to_string("404.html")
       return HttpResponseNotFound(response_data)
