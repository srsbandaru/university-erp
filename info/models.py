from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name="Student Status")
    is_teacher = models.BooleanField(default=False, verbose_name="Teacher Status")

# Department
class Department(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Course 
class Course(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=50, default="X")

    def __str__(self):
        return self.name

