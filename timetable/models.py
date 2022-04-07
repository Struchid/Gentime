from django.db import models


class Group(models.Model):
    class Meta:
        db_table = 'group'
        unique_together = ('number', 'academic_year', 'programme')

    number = models.IntegerField('Group number')
    academic_year = models.CharField(
        'Academic year in roman numerals', max_length=4
    )
    programme = models.CharField('Group programme', max_length=32)
    student_count = models.IntegerField('Number of students in the group')


class Lecturer(models.Model):
    class Meta:
        db_table = 'lecturer'

    PROFESSOR = 'PROF.'
    ASSOCIATE_PROFESSOR = 'A/PROF.'
    LECTURER = 'LECT.'
    ASSISTANT_LECTURER = 'A/LECT.'

    ACADEMIC_RANKS = [
        (PROFESSOR, 'Professor'),
        (ASSOCIATE_PROFESSOR, 'Associate professor'),
        (LECTURER, 'Lecturer'),
        (ASSISTANT_LECTURER, 'Assistant lecturer')
    ]

    name = models.CharField(max_length=128)
    academic_rank = models.CharField(max_length=8, choices=ACADEMIC_RANKS)

    def __str__(self):
        names = self.name.split(' ')
        last_name = names.pop(-1)
        names = '. '.join(name[0] for name in names)

        return f'{self.academic_rank} {names}. {last_name}'


class CourseUnit(models.Model):
    class Meta:
        db_table = 'course_unit'

    name = models.CharField('Course name', max_length=128)
    credit_count = models.FloatField()

    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='courses')


class Student(models.Model):
    class Meta:
        db_table = 'student'

    full_name = models.CharField('Student full name', max_length=128)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Faculty(models.Model):
    class Meta:
        db_table = 'faculty'
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)


class Classroom(models.Model):
    class Meta:
        db_table = 'classroom'

    number = models.CharField('Room number', max_length=8)
    capacity = models.IntegerField()
    building = models.ForeignKey(Faculty, on_delete=models.CASCADE)
