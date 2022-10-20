from .serializers import UserRegisterSerializer, UserDetailsSerializer, UserLoginSerializer
from rest_framework.authtoken.views import Token
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

@api_view(['GET'])
def api_over_view(request):
    data = {
        "Login API" : 'login/',
        "Register API" : 'register/',
        "User details API" : 'user/details/<token>/',
    }
    return Response(data, status=status.HTTP_200_OK)  


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=request.data['email'])
            token = Token.objects.get(user=user)
            return Response({'Token': token.key}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
    return Response({"Error": "Something went wrong!"}, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=request.data['email']):
                return Response({'email': ["A user with that email already exists!"]}, status=status.HTTP_201_CREATED)
            
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            Token.objects.create(user=user)
            return Response({"success": "ok"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
    return Response({"Error": "Something went wrong!"}, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def user_details(request, token):
    if request.method == 'GET':
        token = Token.objects.get(key=token)
        user = User.objects.get(username=token.user.username)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)    
