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
        fields = ('id','status','created_at','expiry_date','note','user','remaining_date')
        read_only_fields =('status','user')

class DonationApprovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationApproved
        fields = ('id','donation','user','decision_date','note','status')
        read_only_fields = ('id','status','decision_date')

    def validate(self,attrs):
        user = attrs.get("user")
        donation = attrs.get("donation")

        if user.role.name != 'evaluator':
            raise serializers.ValidationError({"user":"assign to evaluator user"})

        if user.city != donation.user.city:
            raise serializers.ValidationError({"user":"evaluator should be in the same city"})

        return attrs
    
    def create(self, validated_data):
        donation = validated_data["donation"]
        donation.status = 'processing'
        donation.save()
        donation_approved = DonationApproved.objects.create(**validated_data)
        return donation_approved

class DonationApprovedEvaluatorSerializer(serializers.ModelSerializer):
    status_checkbox = serializers.BooleanField(write_only = True)
    class Meta:
        model = DonationApproved
        fields = '__all__'
        read_only_fields = ('id','donation','user','decision_date','status')
    
    def update(self,instance ,validated_data):
        status_checkbox = validated_data.pop('status_checkbox',None)

        if status_checkbox is None:
            raise serializers.ValidationError("status checkbox doesn't exist")
        if status_checkbox:
            instance.status = 'accepted'
        else:
            instance.status = 'rejected'
        instance.note = validated_data.get('note',instance.note)
        instance.save()
        return instance

# class RestaurantSerializer(serializers.ModelSerializer):
#     donations = DonationSerializer(many = True)
#     class Meta:
#         model = Restaurant
#         fields = ('name','donations',)

# class DonationApprovedSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = DonationApproved
#         fields = '__all__'