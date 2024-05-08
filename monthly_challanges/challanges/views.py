from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render

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
    return HttpResponseRedirect("/challanges/"+redirect_month)

def monthly_ch(request, month):
    try:
        challenge_text = monthly_cha[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("Not valid")
