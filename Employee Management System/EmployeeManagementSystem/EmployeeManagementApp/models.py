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








