from django import forms
from django.forms import ModelForm
from info.models import Department

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['id', 'name']
        labels = {
            "id":"Department ID",
            "name":"Department Name"
        }