from rest_framework import serializers
from .models import Restaurant,Donation,DonationApproved
from django.utils import timezone

class DonationSerializer(serializers.ModelSerializer):
    remaining_date = serializers.SerializerMethodField()
    
    def get_remaining_date(self,obj):
        if obj.expiry_date:
            return  max((obj.expiry_date-timezone.now().date()).days,0)
        return None
    
    class Meta:
        model = Donation
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many = True)
    class Meta:
        model = Restaurant
        fields = ('name','donations',)

class DonationApprovedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DonationApproved
        fields = '__all__'