from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from .models import Course
from django.core.exceptions import ObjectDoesNotExist
def index(request, course_code):
    try:
        course = Course.objects.get(course_code=course_code)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, "CourseEditor/index.html", {'course':course})

def addCourse(request):
    course = Course()
    course.course_name = "New Course"
    course.course_code = "sd"
    course.save()
    return HttpResponseRedirect('editCourse/sd')


