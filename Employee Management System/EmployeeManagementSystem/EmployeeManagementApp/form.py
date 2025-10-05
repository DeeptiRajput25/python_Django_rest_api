from django import forms
from .models import Manager
from .models import Employee


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'email', 'department', 'phone', 'hired_on']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'hired_on': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

        labels = {
            'name': 'Manager Name',
            'email': 'Email Address',
            'department': 'Department',
            'phone': 'Phone Number',
            'hired_on': 'Hire Date',
        }





class EmployeeForm(forms.ModelForm):
    manager = forms.ModelChoiceField(
        queryset=Manager.objects.all(),
        empty_label="Select Manager",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Employee
        fields = ['manager','name', 'email', 'department', 'position', 'salary', 'hired_on']
        widgets = {
            'manager': forms.Select(attrs={  # ✅ Only the widget here
                'class': 'form-control',
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary'
            }),
            'hired_on': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

        labels = {
            'manager': "Manager",
            'name': 'Employee Name',
            'email': 'Email Address',
            'department' :'Department',
            'position': 'Position',
            'salary' : 'salary',
            'hired_on': 'Hire Date',
        }
