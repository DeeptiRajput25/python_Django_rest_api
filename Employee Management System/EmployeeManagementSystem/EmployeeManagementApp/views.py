from django.shortcuts import render

from .form import ManagerForm
from .form import EmployeeForm

def Manager(request):
    print("$$$$$$REquest type is", request.method)
    print("$$$$$$$request data is ", request.POST)
    if request.method == 'POST':
        print('postDetails',request.POST)
        form = ManagerForm(request.POST)
        form.save()


    else:

        form = ManagerForm()
        print("$$$$$",form)
    return render(request, 'Manager_list.html', {'form': form})


def Employee(request):
    if request.method == 'POST':
        print('postDetails', request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
        print("$$$$$",form)


    return render(request, 'employee_list.html', {'form': form})
