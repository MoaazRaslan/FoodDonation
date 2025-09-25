from rest_framework import serializers
from .models import User,Role
from django.contrib.auth import password_validation
from rest_framework import status

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,required = True )
    password2 = serializers.CharField(write_only = True,required = True)
    
    class Meta:
        model = User
        fields = ('id','username','password','password2','phone','city')

    def validate(self, attrs):
        if attrs['password'] != attrs ['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match." })
        
        phone_num = attrs.get('phone')
        if phone_num and not phone_num.isdigit():
            raise serializers.ValidationError({"phone":"phone must be numbers"})     
        
        return super().validate(attrs)

    def create(self,validate_data):
        validate_data.pop('password2')
        role = Role.objects.get(name = 'evaluator')
        print(role)
        print("********************************************************")
        user = User.objects.create_user(**validate_data,role = role)
        return user



class RestaurantRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,required = True )
    password2 = serializers.CharField(write_only = True,required = True)
    
    class Meta:
        model = User
        fields = ('id','username','password','password2','phone','location','city')

    def validate(self, attrs):
        if attrs['password'] != attrs ['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match." })
        
        loc = attrs.get('location')
        if not loc:
            raise serializers.ValidationError({"location":"location must be added"})
        
        phone_num = attrs.get('phone')
        if phone_num and not phone_num.isdigit():
            raise serializers.ValidationError({"phone":"phone must be numbers"})     
        
        return super().validate(attrs)

    def create(self,validate_data):
        validate_data.pop('password2')
        role = Role.objects.get(name = 'restaurant')
        user = User.objects.create_user(**validate_data,role = role)
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','phone','role','city')
    

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','phone','location','role','city')


class RoleSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many = True)
    class Meta:
        model = Role
        fields = ('id','name','users',)

class RestaurantTrusted(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','trusted')
        read_only_fields = ["id"]


    def update(self,instance,validate_data):
        instance.trusted = True
        instance.save()
        return instance

    # def create(self,validate_data):
    #     user = User.objects.get(id = validate_data.get('id'))
    #     if not user:
    #         raise serializers.ValidationError({'user':"not found user"})
    #     user.trusted = True
    #     user.save()
    #     return user