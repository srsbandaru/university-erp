from django import forms
from django.forms import ModelForm
from info.models import Department, Course

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