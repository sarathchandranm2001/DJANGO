from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView 
from .forms import ReviewForm
from .models import Review



# Create your views here.
class ReviewView(CreateView):
    model=Review
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/thank-you"

    #def form_valid(self, form):
     #   form.save()
      #  return super().form_valid(form)
    
    #def get(self, request):
     #   form = ReviewForm()
      #  return render(request, 'reviews/review.html', {"form": form})

    #def post(self, request):
     #   form = ReviewForm(request.POST)
      #  if form.is_valid():
       #     form.save()
        #    return HttpResponseRedirect("/thank-you")
        #return render(request, 'reviews/review.html', {"form": form})

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
    

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        loaded_review=self.object 
        request=self.request
        favourite_id=request.session.get["favourite_review"]
        context["is_favourite"]=favourite_id==str(loaded_review.id)
        return context


    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  review_id=kwargs["id"]
       # selected_review=Review.objects.get(pk=review_id)
        #reviews = Review.objects.all()
        #context["review"] = selected_review
        #return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get('review_id')
        request.session['favourite_review'] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
      