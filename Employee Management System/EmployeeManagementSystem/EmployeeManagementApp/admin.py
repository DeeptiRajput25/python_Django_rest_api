from django.contrib import admin
from .models import Employee
from .models import Manager


# I am registering both em[ployee and manager
admin.site.register(Employee)
admin.site.register(Manager)
