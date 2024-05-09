from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_cha = {
    "january": "January",
    "february": "February",
    "march": "March",
    "april": "April"
}

def index(request):
    list_items = ""
    months = list(monthly_cha.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("Not valid")
