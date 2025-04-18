from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from info.models import Department, Course, Class, Student, User
from allauth.account.models import EmailAddress
from info.forms import DepartmentForm, CourseForm, ClassForm, StudentForm
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
        context["course_list"] = Course.objects.all()
        context["class_list"] = Class.objects.all()
        context["student_list"] = Student.objects.all()
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

# Create Course
class CreateCourse(LoginRequiredMixin, CreateView):
    model = Course 
    form_class = CourseForm 
    template_name = "info/admin/course_form.html"
    success_url = reverse_lazy("info:ManageData")

# Update Course
class UpdateCourse(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['name', 'department', 'short_name']
    template_name = "info/admin/course_form.html"
    success_url = reverse_lazy("info:ManageData")

# Delete Course
class DeleteCourse(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "info/admin/course_confirm_delete.html"
    success_url = reverse_lazy("info:ManageData")

# Create Class
class CreateClass(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = "info/admin/class_form.html"
    success_url = reverse_lazy("info:ManageData")

class UpdateClass(LoginRequiredMixin, UpdateView):
    model = Class
    fields = ['department', 'section', 'semester']
    template_name = "info/admin/class_form.html"
    success_url = reverse_lazy("info:ManageData")

class DeleteClass(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = "info/admin/class_confirm_delete.html"
    success_url = reverse_lazy("info:ManageData")

class CreateStudent(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "info/admin/student_form.html"
    success_url = reverse_lazy("info:ManageData")

    def post(self, request):
        form = StudentForm(request.POST)
        if not form.is_valid():
            context = {"form":form}
            return render(request, self.template_name, context)
        
        # Get all form data
        form_data = request.POST

        # Generate Username : first_name + underscore + last three digits of roll number
        username = form_data["name"].split(" ")[0].lower() + "_" + form_data["roll_number"][-3:]
        print(username)

        # Generate Password : first_name + underscore + year_of_birth
        password = form_data["name"].split(" ")[0].lower() + "_" + form_data["date_of_birth"].replace("-","")[:4]
        print(password)

        # Create a Student in User Model 
        new_user = User.objects.create_user(username = username, password = password, email = form_data["email_address"], is_student = True) 

        # Email Addresses for django allauth
        EmailAddress.objects.create(user = new_user, email = new_user.email, primary = True, verified = False)

        # Create student in student model
        class_id = get_object_or_404(Class, id=form_data["class_id"])
        Student.objects.create(name = form_data["name"], gender = form_data["gender"], roll_number = form_data["roll_number"], date_of_birth = form_data["date_of_birth"], class_id = class_id, user = new_user)

        return redirect(self.success_url)
        

class UpdateStudent(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ["name", "gender", "date_of_birth", "class_id"]
    template_name = "info/admin/student_form.html"
    success_url = reverse_lazy("info:ManageData")

class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "info/admin/student_confirm_delete.html"
    success_url = reverse_lazy("info:ManageData")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        student = User.objects.get(username = self.object.user.username)
        student.delete()
        return redirect(self.success_url)
