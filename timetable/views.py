from django.shortcuts import render

from .models import Group, Lecturer, CourseUnit, Student, Faculty, Classroom


# Landing page
def index(request):
    return render(request, 'index.html')


# Data preparation for schedule generation page
def prepare_data(request):
    groups = Group.objects.all()
    lecturers = Lecturer.objects.all()
    course_units = CourseUnit.objects.all()
    students = Student.objects.all()
    faculties = Faculty.objects.all()
    classrooms = Classroom.objects.all()

    context = {
        'groups': groups,
        'lecturers': lecturers,
        'course_units': course_units,
        'students': students,
        'faculties': faculties,
        'classrooms': classrooms,
    }
    return render(request, 'data_preparation.html', context=context)
