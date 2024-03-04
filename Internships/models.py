from django.contrib.auth.models import AbstractUser
from django.db import models

class DeptUser(AbstractUser):
    dept = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return self.username

class depts(models.Model):
    dept = models.CharField(max_length=30)
    no_of_students = models.IntegerField(default=0)
    no_of_interns = models.IntegerField(default=0)
    no_of_unique_internships = models.IntegerField(default=0)
    def __str__(self):
        return self.dept

class student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.CharField(max_length=30,primary_key=True,null=False)
    year=models.IntegerField()
    section=models.CharField(max_length=6)
    dept=models.CharField(max_length=30)
    def __str__(self):
        return self.rollno

class internships(models.Model):
    rollno = models.ForeignKey(student,on_delete = models.CASCADE)
    internId = models.AutoField(primary_key=True)
    internshipName = models.CharField(max_length=30)
    domain = models.CharField(max_length=40)
    projectName=models.CharField(max_length = 40)
    status=models.CharField(max_length=10)
    sdate = models.DateField()
    edate = models.DateField()
    intern_type = models.CharField(max_length=30)
    certificate = models.CharField(max_length=255)
    def __str__(self):
        return self.intern_type