from django.urls import path
from .views import EmployeeAPIView
from .views import ManagerAPIView
from .views import OfficeListAPIView



urlpatterns =[
    path('employee/',EmployeeAPIView.as_view()),
    path('manager/',ManagerAPIView.as_view()),
    path('OfficeList/', OfficeListAPIView.as_view())

]
