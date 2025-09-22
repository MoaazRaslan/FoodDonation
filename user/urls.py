from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('register/user',views.UserRegisterView.as_view(),name = 'register-user'),
    path('register/restaurant',views.RestaurantRegisterView.as_view(),name = 'register-restaurant'),
    path('login/',TokenObtainPairView.as_view(),name = 'login'),
    # path('',views.UserListView.as_view(),name='get_users'),
    # path('<id>/',views.UserDetailView.as_view()),
    # path('role/',views.RoleListView.as_view(),name='get_roles'),
]

