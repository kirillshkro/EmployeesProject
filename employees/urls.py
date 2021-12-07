from django.urls import path

from employees.views import AddProgLangView, AddDepartmentView
from employees.views import ListEmployees, AddEmployee, EditEmployee, DeleteEmployee

urlpatterns = [
    path('', ListEmployees.as_view(), name='index'),
    path('add/', AddEmployee.as_view(), name='add_employee'),
    path('<int:pk>/edit/', EditEmployee.as_view(), name='edit_employee'),
    path('<int:pk>/delete/', DeleteEmployee.as_view(), name='delete_employee'),
    path('proglang/add/', AddProgLangView.as_view(), name='add_proglang'),
    path('department/add/', AddDepartmentView.as_view(), name='add_department')
]
