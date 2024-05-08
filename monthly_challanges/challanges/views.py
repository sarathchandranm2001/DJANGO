from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_cha = {
    "janaury": "January",
    "february": "February",
    "march": "March",
    "april": "April"

}

# Create your views here.
def monthly_ch_by_num(request,month):
    months=list(monthly_cha.keys())

    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_ch(request, month):
    try:
        challenge_text = monthly_cha[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("Not valid")
