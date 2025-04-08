from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from info.models import Department
from info.forms import DepartmentForm
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'info/index.html'

# Admin Dashboard
class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'info/admin/index.html'

# Teacher Dashboard
class TeacherView(LoginRequiredMixin, TemplateView):
    template_name = 'info/teacher/index.html'

# Student Dashboard
class StudentView(LoginRequiredMixin, TemplateView):
    template_name = 'info/student/index.html'

# Check the Usertype and redirect to respective dashboard
def login_success(request):
    if request.user.is_superuser:
        return redirect("info:AdminView")
    elif request.user.is_teacher:
        return redirect("info:TeacherView")
    elif request.user.is_student:
        return redirect("info:StudentView")
    else:
        return redirect("info:IndexView")

# Manage Data Navigation View
class ManageData(LoginRequiredMixin, TemplateView):
    template_name = "info/admin/manage_data.html"

    def get_context_data(self, **kwargs):
        context = super(ManageData, self).get_context_data(**kwargs)
        context["department_list"] = Department.objects.all()
        return context

# Create Department 
class CreateDepartment(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "info/admin/department_form.html"
    success_url = reverse_lazy("info:ManageData")

# Update Department
class UpdateDepartment(LoginRequiredMixin, UpdateView):
    model = Department
    fields = ['name']
    template_name = "info/admin/department_form.html"
    success_url = reverse_lazy("info:ManageData")
    
# Delete Department
class DeleteDepartment(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = "info/admin/department_confirm_delete.html"
    success_url = reverse_lazy("info:ManageData")