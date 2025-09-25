from rest_framework import serializers
from .models import Donation,DonationApproved
from django.utils import timezone

class DonationSerializer(serializers.ModelSerializer):
    remaining_date = serializers.SerializerMethodField()
    
    def get_remaining_date(self, obj):
        if obj.expiry_date:
            remaining = (obj.expiry_date - timezone.now().date()).days
            return max(0, remaining)  # Return 0 if expired instead of negative
        return None
    
    class Meta:
        model = Donation
        fields = ('status','created_at','expiry_date','note','user','remaining_date')
        read_only_fields =('status','user')

# class RestaurantSerializer(serializers.ModelSerializer):
#     donations = DonationSerializer(many = True)
#     class Meta:
#         model = Restaurant
#         fields = ('name','donations',)

class DonationApprovedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DonationApproved
        fields = '__all__'