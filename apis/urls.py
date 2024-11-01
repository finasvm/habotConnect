from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include
from .views import *

urlpatterns = [
    path('api/employees/',EmployeeAPIView.as_view(),name='employee_create'),
    path('api/employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    


]