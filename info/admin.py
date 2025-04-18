from django.contrib import admin
from info.models import User, Department, Course, Class, Student

# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Student)