from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=20, default='None')
    course_code = models.CharField(max_length=20, default='None')
    course_field_names = ['course_name','course_code']


class Student(models.Model):
    student_name = models.CharField(max_length=20, default='None')
    student_last_name = models.CharField(max_length=20, default='')

    student_code = models.CharField(max_length=20, default='0000000')
    courses = models.ManyToManyField(Course)


