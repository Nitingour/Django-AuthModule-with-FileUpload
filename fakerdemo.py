import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HolidayProject.settings')
import django
django.setup()

from HotelApp.models import *
from faker import Faker
from random import *
fake = Faker('hi_IN')
def insert(n):
    for i in range(n):
        feid=randint(1001,9999)
        fename=fake.name()
        fsalary=randint(10000,999999)
        emp=Employee.objects.get_or_create(eid=feid,ename=fename,salary=fsalary)
     
insert(10)
