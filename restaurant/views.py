from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Donation,DonationApproved
from .serializers import   DonationSerializer,DonationApprovedSerializer,DonationApprovedEvaluatorSerializer
from rest_framework import generics
from rest_framework import permissions 
from common import custom_permissions

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

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

class DonationRestaurantRUDView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [custom_permissions.IsRestaurant]
    
    def get_queryset(self):
        return Donation.objects.filter(user = self.request.user)
    
class DonationSupervisorListView(generics.ListAPIView):
    # queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [custom_permissions.IsSupervisor]
    filterset_fields = ('status',)

    @method_decorator(cache_page(60*15,key_prefix='donation_list'))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        import time
        time.sleep(2)
        return Donation.objects.filter(user__city = self.request.user.city)

class DonationApprovedCreateView(generics.CreateAPIView):
    queryset = DonationApproved.objects.all()
    serializer_class = DonationApprovedSerializer
    permission_classes = [custom_permissions.IsSupervisor]

class DonationApprovedEvaluatorView(generics.RetrieveUpdateAPIView):
    serializer_class = DonationApprovedEvaluatorSerializer
    permission_classes = [custom_permissions.IsEvaluator]

    def get_queryset(self):
        return DonationApproved.objects.filter(user = self.request.user)

class DonationApprovedEvaluatorListView(generics.ListAPIView):
    serializer_class = DonationApprovedSerializer
    permission_classes = [custom_permissions.IsEvaluator]

    def get_queryset(self):
        return DonationApproved.objects.filter(user = self.request.user)

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


