from EmployeeManagementApp.models import Employee
from EmployeeManagementApp.models import Manager
from EmployeeManagementApp.models import OfficeList
from EmployeeManagementApp.models import Attendance
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee
        fields='__all__'



class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Manager
        fields='__all__'


class OfficeListSerializer(serializers.ModelSerializer):

    class Meta:
        model=OfficeList
        fields='__all__'


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Attendance
        fields='__all__'