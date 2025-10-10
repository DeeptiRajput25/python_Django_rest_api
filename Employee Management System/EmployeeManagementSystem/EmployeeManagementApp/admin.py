from django.contrib import admin
from .models import Employee
from .models import Manager
from .models import OfficeList
from .models import Attendance




# I am registering both em[ployee and manager
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(OfficeList)
admin.site.register(Attendance)




