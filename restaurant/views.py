from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurant,Donation
from .serializers import RestaurantSerializer , DonationSerializer

@api_view(['GET'])
def get_restaurants(request):
    rest = Restaurant.objects.all()
    serializer = RestaurantSerializer(rest,many = True)
    return Response({'data':serializer.data})
