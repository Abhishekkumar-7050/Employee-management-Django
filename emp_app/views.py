from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
# Create your views here.
from . models import Role , Employee , Department
from .forms import Employeeform


def index(request):
    return render(request , 'index.html')

def all_emp(request):

    

    employees = Employee.objects.all()
  

    return render(request, 'all_emp.html', {'employees': employees})

def remove_emp(request):
    employees = Employee.objects.all()
    return render(request, 'remove_emp.html',{'employees': employees})

def add_emp(request):
    if request.method == "POST" :
       form = Employeeform(request.POST)   # Step 2: Bind form data 
       if form.is_valid :
           form.save() 
           return redirect('all_emp')
    else:
        form = Employeeform()
        
    return render(request, 'add_emp.html', {'form': form})


# Inside form.save():
# Django creates a new Employee object in memory.
# It assigns values from request.POST to the object.
# Django executes an SQL INSERT query to save the object in the database.
# The saved object now exists in the database.

    



def filter_emp(request):
    return render(request,'filter_emp.html')






def delete_employee(request, emp_id):
    try:
        employee = get_object_or_404(Employee, id=emp_id)  # Get employee by ID
    except Http404:
        return render(request, 'error.html', {'message': 'Employee not found'})  # Custom error page

    if request.method == 'POST':  # Confirm delete action
        employee.delete()
        return redirect('all_emp')  # Redirect to employee list after deletion

    return render(request, 'confirm_delete.html', {'employee': employee}) 





def filter_employee(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    roles = Role.objects.all()

    # Get filter values from request
    department_id = request.GET.get('department')
    role_id = request.GET.get('role')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    # Apply filters
    if department_id and department_id != "all":
        employees = employees.filter(dept__id=department_id)

    if role_id and role_id != "all":
        employees = employees.filter(role__id=role_id)

    if min_salary:
        employees = employees.filter(salary__gte=min_salary)

    if max_salary:
        employees = employees.filter(salary__lte=max_salary)

    context = {
        'employees': employees,
        'departments': departments,
        'roles': roles,
    }

    return render(request, 'filter_employee.html', context)