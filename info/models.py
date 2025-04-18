from django.db import models
from django.contrib.auth.models import AbstractUser

# Constants
gender_choices = (
    ("Male", "Male"),
    ("Female", "Female")
)

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

# Class   
class Class(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    id = models.CharField(max_length=50, primary_key=True)
    section = models.CharField(max_length=200)
    semester = models.IntegerField()

    def __str__(self):
        dept = Department.objects.get(name = self.department)
        return dept.name + " : " + str(self.semester) + " " + self.section
    
# Student
class Student(models.Model):
    roll_number = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50, choices=gender_choices, default="Male")
    date_of_birth = models.DateField(default="2007-02-12")
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
