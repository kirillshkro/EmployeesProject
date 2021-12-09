from django.db import models


# Create your models here.


class ProgrammingLanguageModel(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=True)

    def __str__(self):
        return self.title


class DepartmentModel(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=True)
    floor = models.IntegerField(blank=False)

    def __str__(self):
        return self.title


class EmployeeModel(models.Model):
    class Sex(models.TextChoices):
        Male = "МУЖ", "Мужской",
        Female = "Жен.", "Женский"

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField(blank=False, null=False)
    sex = models.CharField(max_length=10, blank=False, choices=Sex.choices, verbose_name='Пол')
    department = models.ForeignKey('DepartmentModel', on_delete=models.CASCADE, blank=True, null=True)
    programming_language = models.ForeignKey('ProgrammingLanguageModel', on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='first_last_name')
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name
