from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import *
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404

# Create your views here.


class EmployeeAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        department=request.query_params.get('department')
        role=request.query_params.get('role')
        employees=Employee.objects.all()

        # Filter by department and role
        if department:
            employees=Employee.objects.filter(department=department)
        if role:
            employees=Employee.objects.filter(role=role)

        # Paginate results (10 employees per page)
        paginator = Paginator(employees, 10)
        page_number = request.query_params.get('page', 1)
        
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer=Employeeserializer(page,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        employee=get_object_or_404(Employee,id=pk)
        serializer=Employeeserializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        employee=get_object_or_404(Employee,id=pk)
        serializer=Employeeserializer(employee,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(Self,request,pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
