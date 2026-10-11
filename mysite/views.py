from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(request, 'home.html', context)
