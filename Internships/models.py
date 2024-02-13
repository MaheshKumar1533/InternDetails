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