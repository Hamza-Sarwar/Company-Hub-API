from rest_framework import serializers
from .models import Company, Employee, EmploymentHistory


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'established_date']
        read_only_fields = ['id']

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'company_name', 'hire_date', 'is_active']
        read_only_fields = ['id']

    def validate_email(self, value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'hire_date', 'is_active']

    def validate_company(self, value):
        if not value:
            raise serializers.ValidationError("Company is required.")
        return value

class EmploymentHistorySerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = EmploymentHistory
        fields = ['id', 'employee_name', 'company_name', 'start_date', 'end_date', 'job_title', 'salary']
        read_only_fields = ['id']

class EmploymentHistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmploymentHistory
        fields = ['employee', 'company', 'start_date', 'end_date', 'job_title', 'salary']
