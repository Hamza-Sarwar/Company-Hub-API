from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    established_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Companies'
        verbose_name = 'Company'
        ordering = ['name']
        db_table = 'company'

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    hire_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Employees'
        verbose_name = 'Employee'
        ordering = ['first_name', 'last_name']
        db_table = 'employee'
        indexes = [models.Index(fields=['email'], name='employee_email_idx')]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmploymentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employment_histories')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employment_histories')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Employment Histories'
        verbose_name = 'Employment History'
        db_table = 'employment_history'


    def __str__(self):
        return f"{self.employee} {self.company} {self.start_date} {self.end_date}"






