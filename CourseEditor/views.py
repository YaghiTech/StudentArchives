from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from .models import Course
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    all_courses = Course.objects.all()
    if request.method == 'POST':
        for course in all_courses:
            if request.POST.get(str(course.id)):
                return HttpResponseRedirect('/editCourse/course/' + str(course.id))

    return render(request, "CourseEditor/index.html", {'all_courses': all_courses})


def edit_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        changed = False

        for name in Course.course_field_names:
            request_text = request.POST.get(name, None)
            if request_text is not None and request_text is not '':
                setattr(course, name, request_text)
                course.save()
                changed = True
        if changed:
            return HttpResponseRedirect('/editCourse/')

    course.save()
    return render(request, "CourseEditor/editCourse.html", {'course': course})

def add_course(request):
    course = Course()
    course.course_name = "New Course"
    course.course_code = "00000"
    course.save()
    return HttpResponseRedirect('/editCourse/course/'+str(course.id))


