from django.urls import path
from . import views

urlpatterns = [
    path('',views.DonationListCreateView.as_view()),
]