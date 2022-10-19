from rest_framework.authtoken.views import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import UserRegisterSerializer, UserDetailsSerializer
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            pass
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)  

"""
{
    "username" : "athie",
    "email" : "athie@g.co",
    "role" : "admin",
    "country" : "india",
    "nationality" : "india",
    "mobile_no" : "9098909877",
    "password" : "1234",
    "confirm_password" : "1234"
}
"""

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=request.data['email']):
                return Response({'Error': "A user with that email already exists!"}, status=status.HTTP_400_BAD_REQUEST)
            if request.data['password'] != request.data['confirm_password']:
                return Response({'Error': "Password not matching!"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            Token.objects.create(user=user)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
        return Response({"Success": "ok"}, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def user_details(request, token):
    if request.method == 'GET':
        token = Token.objects.get(key=token)
        user = User.objects.get(username=token.user.username)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)    
