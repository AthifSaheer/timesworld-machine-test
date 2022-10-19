from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', obtain_auth_token),
    path('user/details/<str:token>/', views.user_details, name='user_details'),
]
