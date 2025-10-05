from django.contrib import admin
from .models import Employee
from .models import Manager



admin.site.register(Employee)
admin.site.register(Manager)