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
    path("admin_home/manage_data/course/create", views.CreateCourse.as_view(), name = "CreateCourse"),
    path("admin_home/manage_data/course/update/<str:pk>", views.UpdateCourse.as_view(), name = "UpdateCourse"),
    path("admin_home/manage_data/course/delete/<str:pk>", views.DeleteCourse.as_view(), name = "DeleteCourse"),
    path("admin_home/manage_data/class/create", views.CreateClass.as_view(), name = "CreateClass"),
    path("admin_home/manage_data/class/update/<str:pk>", views.UpdateClass.as_view(), name = "UpdateClass"),
    path("admin_home/manage_data/class/delete/<str:pk>", views.DeleteClass.as_view(), name = "DeleteClass"),
    path("admin_home/manage_data/student/create", views.CreateStudent.as_view(), name = "CreateStudent"),
    path("admin_home/manage_data/student/update/<str:pk>", views.UpdateStudent.as_view(), name = "UpdateStudent"),
    path("admin_home/manage_data/student/delete/<str:pk>", views.DeleteStudent.as_view(), name = "DeleteStudent"),
]