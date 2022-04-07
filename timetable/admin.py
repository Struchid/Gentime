from django.contrib import admin

from .models import Group, Lecturer, CourseUnit, Student, Faculty, Classroom

admin.site.register(Group)
admin.site.register(Lecturer)
admin.site.register(CourseUnit)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Classroom)
