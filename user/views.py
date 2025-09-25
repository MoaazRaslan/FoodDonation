from django.shortcuts import render
from django.http import JsonResponse
from .models import User,Role
from .serializers import UserSerializer,RoleSerializer,UserRegisterSerializer,RestaurantSerializer,RestaurantRegisterSerializer,RestaurantTrusted
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework import permissions
from rest_framework.views import APIView
from common import custom_filters,custom_permissions
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
    # permission_classes = [permissions.IsAdminUser]
    filterset_class = custom_filters.UserFilter
    # filterset_fields = ('phone',)    

class EvaluatorPromotionView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [custom_permissions.IsSupervisor|permissions.IsAdminUser]
    def update(self,request,*args,**kwargs):
        user = self.get_object()
        role = user.role
        new_role = Role.objects.get(name = 'supervisor')
        evaluator_role =Role.objects.get(name = 'evaluator')

        if role == new_role :
            return Response({"Role":"user is already a supervisor"},status=status.HTTP_400_BAD_REQUEST)
        
        if role != evaluator_role:
            return Response({"Role":"user should be an evaulator"},status=status.HTTP_400_BAD_REQUEST)

        user.role = new_role
        user.save()
        return Response(self.serializer_class(user).data,status=status.HTTP_200_OK)

class UserTrustedView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RestaurantTrusted
    permission_classes = [custom_permissions.IsSupervisor | permissions.IsAdminUser]

class RestaurantListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [custom_permissions.IsSupervisor]

    def get_queryset(self):
        return User.objects.filter(role = Role.objects.get(name = 'restaurant'))

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer






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