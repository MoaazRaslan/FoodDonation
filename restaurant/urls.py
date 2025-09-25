from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.DonationCreateView.as_view()),
    path('list/',views.DonationRestaurantListView.as_view()),

]