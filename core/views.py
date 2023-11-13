from django.shortcuts import render,redirect
from .forms import PositionForm,EmployeeForm
from .models import Position,Employee
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

#Add position view
def add_position_view(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save()
            messages.info(request, 'Successfully added the '+form.cleaned_data['position']+' position.')
            return redirect('manage-positions')
        else:
            messages.error(request, 'Failed to add position.')
            return redirect('add-position')

    else:
        form = PositionForm()
        return render(request,'forms/add_position.html',{
            'form':form,
        })

#Update position view
def update_position_view(request,id):
    if request.method == 'POST':
        position = Position.objects.get(pk=id)
        form = PositionForm(request.POST,instance=position)
        if form.is_valid():
            updated_position = form.save()
            messages.info(request, 'Successfully updated the '+form.cleaned_data['position']+' position details.')
            return redirect('manage-positions')
        else:
            messages.error(request, 'Failed to update position details.')
            return redirect('edit-position',id)

    else:
        position = Position.objects.get(pk=id)
        form = PositionForm(instance=position)
        return render(request,'forms/update_position.html',{
            'form':form,
            'position':position,
        })

#Delete Position view
def delete_position_view(request,id):
    position = Position.objects.get(pk=id)
    position.delete()
    messages.info(request, 'Successfully deleted the '+form.cleaned_data['position']+' position.')
    return redirect('manage-positions')

#manage positions
def manage_positions_view(request):
    positions = Position.objects.all()
    return render(request,"manage/manage_positions.html",{
        'positions':positions,
    })

#Add employee view
def add_employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.info(request, 'Successfully added the employee '+form.cleaned_data['first_name']+' '+form.cleaned_data['last_name']+'.')
            return redirect('manage-employees')
        else:
            messages.error(request, 'Failed to added employee '+form.cleaned_date['first_name']+' '+form.cleaned_date['last_name']+'.')
            return redirect('add-employee')

    else:
        form = EmployeeForm()
        return render(request,'forms/add_employee.html',{
            'form':form,
        })


#Update employee view
def update_employee_view(request,id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            updated_employee = form.save()
            messages.info(request, 'Successfully updated the employee '+form.cleaned_data['first_name']+' '+form.cleaned_data['last_name']+ '.')
            return redirect('manage-employees')
        else:
            messages.error(request, 'Failed to add employee.')
            return redirect('edit-employee',id)

    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        return render(request,'forms/update_employee.html',{
            'form':form,
            'employee':employee,
        })

#Delete Employee view
def delete_employee_view(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    messages.info(request, 'Successfully deleted the employee '+form.cleaned_data['first_name']+' '+form.cleaned_data['last_name']+'.')
    return redirect('manage-employees')

#manage employees
def manage_employees_view(request):
    employees = Employee.objects.all()
    return render(request,"manage/manage_employees.html",{
        'employees':employees,
    })

