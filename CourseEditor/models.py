from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20, default='None')
    course_code = models.CharField(max_length=20, default='None')
