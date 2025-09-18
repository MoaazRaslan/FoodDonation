from rest_framework import serializers
from .models import User,Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def validate_phone(self, values):
        if not values.isdigit():
            raise serializers.ValidationError("phone must be a number")
        return values
    
class RoleSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many = True)
    class Meta:
        model = Role
        fields = (
            'id',
            'name',
            'users',
        )
