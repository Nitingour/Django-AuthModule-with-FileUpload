from django.contrib import admin
from HotelApp.models import Employee
#from HotelApp import models.Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','salary']
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
