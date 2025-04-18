from django import forms
from django.forms import ModelForm
from info.models import Department, Course, Class, Student

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['id', 'name']
        labels = {
            "id":"Department ID",
            "name":"Department Name"
        }

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'short_name']
        labels = {
            "id":"Course ID",
            "name":"Course Name",
        }

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['department', 'id', 'section', 'semester']
        labels = {
            "id":"Class ID",
            "section":"Class Section",
            "semester":"Class Semester"
        }

class StudentForm(ModelForm):
    email_address = forms.EmailField()
    class Meta:
        model = Student
        fields = ['roll_number', 'name', 'gender', 'date_of_birth', 'class_id']
        labels = {
            "roll_number":"Student Roll Number",
            "name":"Student Full Name",
            "date_of_birth":"Date of Birth",
            "class_id":"Class"
        }
        widgets = {
            'date_of_birth':forms.DateInput(attrs={"type":"date"})
        }

