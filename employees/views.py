import json

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from employees.forms import AddEmployeeForm, EditEmployeeForm, AddPLForm, AddDepartmentForm
from employees.models import EmployeeModel, ProgrammingLanguageModel, DepartmentModel


# Create your views here.


class ListEmployees(ListView):
    template_name = 'employees/index.html'
    model = EmployeeModel
    context_object_name = 'employee_list'


class DeleteEmployee(DeleteView):
    model = EmployeeModel
    template_name = 'employees/delete_employee.html'
    success_url = reverse_lazy('index')
    context_object_name = 'employee'


class AddEmployee(CreateView):
    template_name = 'employees/add_employee.html'
    form_class = AddEmployeeForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddEmployee, self).get_context_data(**kwargs)
        results = []
        for item in EmployeeModel.objects.all():
            results.append(item.first_name)
        context['names'] = json.dumps(results)
        return context


class EditEmployee(UpdateView):
    template_name = 'employees/edit_employee.html'
    form_class = EditEmployeeForm
    success_url = '/'
    model = EmployeeModel


class AddProgLangView(CreateView):
    template_name = 'employees/admin/add_programming_language.html'
    form_class = AddPLForm
    model = ProgrammingLanguageModel
    success_url = '/'


class AddDepartmentView(CreateView):
    template_name = 'employees/admin/add_department.html'
    form_class = AddDepartmentForm
    model = DepartmentModel
    success_url = '/'
