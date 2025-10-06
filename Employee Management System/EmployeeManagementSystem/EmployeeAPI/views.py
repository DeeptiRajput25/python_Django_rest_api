from rest_framework import generics
from EmployeeManagementApp.models import Employee
from EmployeeManagementApp.models import Manager
from EmployeeManagementApp.models import OfficeList


from .serializers import EmployeeSerializer
from .serializers import ManagerSerializer
from .serializers import OfficeListSerializer



class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ManagerAPIView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class OfficeListAPIView(generics.ListCreateAPIView):
    queryset = OfficeList.objects.all()
    serializer_class = OfficeListSerializer