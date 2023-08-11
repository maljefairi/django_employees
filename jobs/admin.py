from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Employee
from django.contrib import admin


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee


class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource


admin.site.register(Employee, EmployeeAdmin)
