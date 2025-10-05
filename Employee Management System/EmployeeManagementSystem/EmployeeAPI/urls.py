from django.urls import path
from .views import EmployeeAPIView
from .views import ManagerAPIView


urlpatterns =[
    path('employee/',EmployeeAPIView.as_view()),
    path('manager/',ManagerAPIView.as_view())
]
