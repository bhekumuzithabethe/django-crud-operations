from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    #Position urls
    path('add-position/',views.add_position_view,name='add-position'),#Add Position url
    path('update-position/<int:id>/',views.update_position_view,name='update-position'),#Update Position url
    path('delete-position/<int:id>/',views.delete_position_view,name='delete-position'),#Delete Position url
    path('manage-positions/',views.manage_positions_view,name='manage-positions'),#Manage Positions url

    #Employee urls
    path('add-employee/',views.add_employee_view,name='add-employee'),#Add Employee url
    path('update-employee/<int:id>/',views.update_employee_view,name='update-employee'),#Update Employee url
    path('delete-employee<int:id>/',views.delete_employee_view,name='delete-employee'),#Delete Employee url
    path('manage-employees/',views.manage_employees_view,name='manage-employees'),#Manage Employees url

]
