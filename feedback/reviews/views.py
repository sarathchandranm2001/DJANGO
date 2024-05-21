from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .forms import ReviewForm
from .models import Review



# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, 'reviews/review.html', {"form": form})

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'This works'
        return context

class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model=Review
    context_object_name="reviews"

    #def get_queryset(self):
     #   base_query=super().get_queryset()
      #  data=base_query.filter(rating__gt=4)
       # return data

   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   reviews = Review.objects.all()
      #  context["reviews"] = reviews
       # return context
    

class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id=kwargs["id"]
        selected_review=Review.objects.get(pk=review_id)
        reviews = Review.objects.all()
        context["review"] = selected_review
        return context
    
