from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.contrib.auth.models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import status
User = get_user_model()

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        # return Response(srlzr.data, status=status.HTTP_201_CREATED)
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
        try:
            username = request.data['username']
        except KeyError:
            return Response({'Error': "Username is a required field!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            email = request.data['email']
        except KeyError:
            return Response({'Error': "Email is a required field!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            role = request.data['role']
        except KeyError:
            return Response({'Error': "Role is a required field!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            country = request.data['country']
        except KeyError:
            return Response({'Error': "Country is a required field!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            nationality = request.data['nationality']
        except KeyError:
            return Response({'Error': "Nationality is a required field!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            mobile_no = request.data['mobile_no']
        except KeyError:
            return Response({'Error': "Mobile no is a required field!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            password = request.data['password']
        except KeyError:
            return Response({'Error': "Password is a required field!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            confirm_password = request.data['confirm_password']
        except KeyError:
            return Response({'Error': "Confirm password is a required field!"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username) or User.objects.filter(email=email):
            return Response({'Error': "Username/Email already exist!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({'Error': "Password not matching!"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create(username=username, email=email, role=role, country=country, nationality=nationality, mobile_no=mobile_no, password=password)

        return Response({}, status=status.HTTP_201_CREATED)
    