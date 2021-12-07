from django import forms
from django.core import validators

from employees.models import EmployeeModel, DepartmentModel, ProgrammingLanguageModel


class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(
        attrs={id: 'fname'}
    ))
    last_name = forms.CharField(label='Фамилия', required=True)
    age = forms.IntegerField(label='Возраст', required=True, validators=[
        validators.MinValueValidator(limit_value=16)
    ])
    department = forms.ModelChoiceField(label='Отдел', queryset=DepartmentModel.objects.all(),
                                        empty_label='Выберите отдел')
    sex = forms.ChoiceField(label='Пол', choices=EmployeeModel.Sex.choices)
    programming_language = forms.ModelChoiceField(label='Язык программирования',
                                                  queryset=ProgrammingLanguageModel.objects.all(),
                                                  empty_label='Выберите язык')

    class Meta:
        model = EmployeeModel
        fields = '__all__'


class EditEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', required=True)
    last_name = forms.CharField(label='Фамилия', required=True)
    age = forms.IntegerField(label='Возраст', required=True, validators=[
        validators.MinValueValidator(limit_value=16)
    ])
    department = forms.ModelChoiceField(label='Отдел', queryset=DepartmentModel.objects.all())
    programming_language = forms.ModelChoiceField(label='Язык программирования',
                                                  queryset=ProgrammingLanguageModel.objects.all())

    class Meta:
        model = EmployeeModel
        fields = ('first_name', 'last_name', 'age', 'department', 'programming_language',)


'''Добавляем язык программирования в справочник'''


class AddPLForm(forms.ModelForm):
    title = forms.CharField(max_length=150, min_length=1, label='Язык программирования')

    class Meta:
        model = ProgrammingLanguageModel
        fields = '__all__'


'''Добавляем отдел в справочник'''


class AddDepartmentForm(forms.ModelForm):
    title = forms.CharField(max_length=150, min_length=1, label='Отдел')
    floor = forms.IntegerField(min_value=0, label='Этаж')

    class Meta:
        model = DepartmentModel
        fields = '__all__'
