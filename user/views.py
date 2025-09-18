from django.shortcuts import render
from django.http import JsonResponse
from .models import User,Role
from .serializers import UserSerializer,RoleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user,many = True)
    return Response({'user':serializer.data})

@api_view(['GET'])
def get_roles(request):
    role = Role.objects.all()
    serializer = RoleSerializer(role,many = True)
    return Response({'role':serializer.data})