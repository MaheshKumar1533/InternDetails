from django.contrib.auth.models import AbstractUser
from django.db import models

class DeptUser(AbstractUser):
    dept = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username
class depts(models.Model):
    dept = models.CharField(max_length=30)
    def __str__(self):
        return self.dept
    
class student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.CharField(max_length=30,primary_key=True,null=False)
    year=models.IntegerField()
    dept=models.CharField(max_length=30)
    photo = models.ImageField(upload_to='imagesstudent/')
    def __str__(self):
        return self.rollno

class internships(models.Model):
    rollno = models.ForeignKey(student,on_delete = models.CASCADE)
    internId = models.AutoField(primary_key=True)
    internshipName = models.CharField(max_length=30)
    sdate = models.DateField()
    edate = models.DateField()
    type = models.CharField(max_length=30)
    certificate = models.ImageField(upload_to='certificates/')
    def __str__(self):
        return self.internId