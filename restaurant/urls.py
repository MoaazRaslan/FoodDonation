from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.DonationCreateView.as_view()),
    path('list/',views.DonationRestaurantListView.as_view()),
    path('donation/<pk>',views.DonationRestaurantRUDView.as_view()),
    path('donation_supervisor/',views.DonationSupervisorListView.as_view()),
    path('donation_approved_create/',views.DonationApprovedCreateView.as_view()),
    path('donation_approved_evaluator/<pk>/',views.DonationApprovedEvaluatorView.as_view()),
    path('donation_approved_list_evaluator/',views.DonationApprovedEvaluatorListView.as_view()),
]