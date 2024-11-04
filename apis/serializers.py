from rest_framework import serializers
from .models import Employee

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= ['id','name', 'email', 'department', 'role', 'date_joined']

    def validate_name(self,value):
        if not value.strip():
            raise serializers.ValidationError('name should not be empty')
        return value
    def validate_email(self,value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError('email is already taken')
        return value
    
