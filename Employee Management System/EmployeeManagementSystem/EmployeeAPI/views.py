from rest_framework import generics
from EmployeeManagementApp.models import Employee
from EmployeeManagementApp.models import Manager

from .serializers import EmployeeSerializer
from .serializers import ManagerSerializer


class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerAPIView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer