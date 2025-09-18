from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_users,name='get_users'),
    path('role/',views.get_roles,name='get_roles'),
]

