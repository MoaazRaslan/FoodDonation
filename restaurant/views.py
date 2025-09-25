from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Donation
from .serializers import   DonationSerializer
from rest_framework import generics
from rest_framework import permissions 
from common import custom_permissions

class DonationCreateView(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [custom_permissions.IsRestaurant]
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class DonationRestaurantListView(generics.ListAPIView):
    # queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [custom_permissions.IsRestaurant]
    
    def get_queryset(self):
        return Donation.objects.filter(user = self.request.user)



# class DonationListCreateView(generics.ListCreateAPIView):
#     queryset = Donation.objects.all()
#     serializer_class = DonationSerializer

#     def get_permissions(self):
#         self.permission_classes = [permissions.AllowAny]
#         if self.request.method == 'POST':
#             self.permission_classes = [permissions.IsAuthenticated]
#         return super().get_permissions()
    


# @api_view(['GET'])
# def get_restaurants(request):
#     rest = Restaurant.objects.all()
#     serializer = RestaurantSerializer(rest,many = True)
#     return Response({'data':serializer.data})


