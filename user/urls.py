from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('register/user',views.UserRegisterView.as_view(),name = 'register-user'),
    path('register/restaurant',views.RestaurantRegisterView.as_view(),name = 'register-restaurant'),
    path('login/',TokenObtainPairView.as_view(),name = 'login'),
    
    path('trusted/<pk>/',views.UserTrustedView.as_view(),name="restaurant-trusted"),
    path('evaluator_promote/<pk>/',views.EvaluatorPromotionView.as_view(),name='evaulator-promote'),
    path('list_restaurant/',views.RestaurantListView.as_view(),name='get-restaurant'),
    path('user_profile/<pk>',views.UserDetailView.as_view(),name='user-detail'),
    path('list_user',views.UserListView.as_view(),name='get-users'),

    # path('<id>/',views.UserDetailView.as_view()),
    # path('role/',views.RoleListView.as_view(),name='get_roles'),
]

