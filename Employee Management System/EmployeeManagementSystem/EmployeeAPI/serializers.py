from EmployeeManagementApp.models import Employee
from EmployeeManagementApp.models import Manager
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee
        fields='__all__'



class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Manager
        fields='__all__'