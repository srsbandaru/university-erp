from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("", views.IndexView.as_view(), name = "IndexView"),
    path("login_success/", views.login_success, name = "login_success"),
    path("admin_home/", views.AdminView.as_view(), name = "AdminView"),
    path("teacher/", views.TeacherView.as_view(), name = "TeacherView"),
    path("student/", views.StudentView.as_view(), name = "StudentView"),
    path("admin_home/manage_data/", views.ManageData.as_view(), name = "ManageData"),
    path("admin_home/manage_data/department/create", views.CreateDepartment.as_view(), name = "CreateDepartment"),
    path("admin_home/manage_data/department/update/<str:pk>", views.UpdateDepartment.as_view(), name = "UpdateDepartment"),
    path("admin_home/manage_data/department/delete/<str:pk>", views.DeleteDepartment.as_view(), name = "DeleteDepartment"),
]