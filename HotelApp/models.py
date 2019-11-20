from django.db import models
# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    salary=models.FloatField()


class Upload(models.Model):
    name=models.CharField(max_length=50)
    pic=models.FileField(upload_to='images/')
    author=models.CharField(max_length=50)
    uploaddate=models.DateTimeField(auto_now_add=True)
