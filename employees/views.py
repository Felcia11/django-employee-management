from django.http import Http404,HttpResponse
from django.shortcuts import get_object_or_404, render
from employees.models import Employee


# Create your views here.
def employee_detail(request, pk):
    employee = get_object_or_404(Employee,pk=pk)
    context={
        'employee':employee
    }
    return render(request,'employee_detail.html',context)
