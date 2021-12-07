from django.contrib import admin

from employees.models import ProgrammingLanguageModel, DepartmentModel, EmployeeModel

# Register your models here.

admin.site.register(ProgrammingLanguageModel)
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)
