from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),  # class-based view implementation
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewsListView.as_view(), name='review-list'),
    #path('reviews/<int:id>/', views.SingleReviewView.as_view(), name='single-review')-for listviews,
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='single-review'),#detailview 
    
]