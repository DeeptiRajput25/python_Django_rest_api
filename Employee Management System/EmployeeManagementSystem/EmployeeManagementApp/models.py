from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    hired_on = models.DateField()

    def __str__(self):
        return self.name



class Employee(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hired_on = models.DateField()

    def __str__(self):
        return self.name



class OfficeList(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    contact_person = models.CharField(max_length=50)

    def __str__(self):
        return self.address




# class Attendance(models.Model):
#     employeeName = models.CharField(max_length=100)
#     date = models.DateField()
#     present = models.BooleanField(default=False)
#     absent = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.address



class Attendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
            ('sickleave','fsdfd')
        ],
        default='Present'
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"








