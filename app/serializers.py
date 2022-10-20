from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role', 'country', 'nationality', 'mobile_no']

    def create(self , validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'], role=validated_data['role'], country=validated_data['country'], nationality=validated_data['nationality'], mobile_no=validated_data['mobile_no'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'country', 'nationality', 'mobile_no']