from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Employee

# Create your views here.


def homepage(request):
    if request.method == 'POST':
        # print(request.POST)
        id = request.POST.get('eid')
        name = request.POST.get('ename')
        age = request.POST.get('eage')
        salary = request.POST.get('esalary')
        address = request.POST.get('eaddress')
        is_active = request.POST.get('eactive')
        if is_active == 'on':
            is_active = True
        else:
            is_active = False
        if not id:
            emp = Employee(name=name, age=age, salary=salary, address=address, is_active=is_active)
            emp.save()
            return redirect('show_emp')
        else:
            emp = Employee.objects.get(id=id)
            emp.name = name
            emp.age = age
            emp.salary = salary
            emp.address = address
            emp.is_active = is_active
            emp.save()
            return redirect('show_emp')
    else:
        return render(request, 'home.html')


def edit_emp(request, pk):
    emp = Employee.objects.get(id=pk)
    return render(request, 'home.html', {'emp':emp})
    
def show_employee(request):
    emps = Employee.objects.all()
    return render(request, 'show_emp.html', {'emps':emps})

def active_emp(request):
    emps = Employee.active_data()
    return render(request, 'show_emp.html', {'emps':emps})