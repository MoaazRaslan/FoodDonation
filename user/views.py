from django.shortcuts import render
from django.http import JsonResponse
from .models import User,Role
from .serializers import UserSerializer,RoleSerializer,UserRegisterSerializer,RestaurantSerializer,RestaurantRegisterSerializer,RestaurantTrusted
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
import custom_permissions
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class RestaurantRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RestaurantRegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
class RestuarantTrustedView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RestaurantTrusted
    permission_classes = [custom_permissions.IsSupervisor]








class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'id'

class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# @api_view(['GET'])
# def get_users(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user,many = True)
#     return Response({'user':serializer.data})

# @api_view(['GET'])
# def get_roles(request):
#     role = Role.objects.all()
#     serializer = RoleSerializer(role,many = True)
#     return Response({'role':serializer.data})









        # return super().has_permission(request, view)