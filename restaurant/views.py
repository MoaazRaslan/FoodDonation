from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurant,Donation
from .serializers import RestaurantSerializer , DonationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    


# @api_view(['GET'])
# def get_restaurants(request):
#     rest = Restaurant.objects.all()
#     serializer = RestaurantSerializer(rest,many = True)
#     return Response({'data':serializer.data})


