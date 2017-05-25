from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from .models import Course, Student
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


def index(request):
    all_courses = Course.objects.all()
    if request.method == 'POST':
        for course in all_courses:
            if request.POST.get('view'+str(course.id)):
                return HttpResponseRedirect('/courseList/course/' + str(course.id))
            if request.POST.get('edit'+str(course.id)):
                return HttpResponseRedirect('/courseList/editCourse/' + str(course.id))
            if request.POST.get('add_course'):
                return HttpResponseRedirect('/courseList/addCourse/' + str(course.id))
    return render(request, "CourseEditor/index.html", {'all_courses': all_courses})


def view_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        if request.POST.get('add_student'):
            return HttpResponseRedirect('/courseList/course/' + course_id + '/addStudent')
    return render(request, "CourseEditor/viewCourse.html", {'course': course, 'add_student' : 'False',
                                                            'all_students': Student.objects.filter(courses__id=course_id)})


def edit_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        for name in Course.course_field_names:
            request_text = request.POST.get(name, None)
            if request_text is not None and request_text is not '':
                setattr(course, name, request_text)
                course.save()
        return HttpResponseRedirect('/courseList/')

    course.save()
    return render(request, "CourseEditor/editCourse.html", {'course': course, 'add_student' : 'True'})


def add_student(request,course_id):
    try:
        course = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        request_text = request.POST.get('new_student', None)
        if request_text == '' or request_text is None:
            return HttpResponseRedirect('/courseList/course/' + course_id)
        else:
            try:
                try:
                    Student.objects.get(courses__id=course_id,student_name=request_text.split()[0],
                                        student_last_name=request_text.split()[1])

                    return render(request, "CourseEditor/viewCourse.html",
                                  {'course': course,
                                   'all_students': Student.objects.all().filter(courses__id=course_id),
                                   'suggest_students': Student.objects.all().filter(~Q(courses__id=course_id)),
                                   'duplicate_student': 'True'})

                except ObjectDoesNotExist:
                    student = Student.objects.get(student_name=request_text.split()[0],
                                                  student_last_name=request_text.split()[1])
                    student.courses.add(course)
                    student.save()
            except ObjectDoesNotExist:
                new_student = Student()
                new_student.student_name, new_student.student_last_name = request_text.split()
                new_student.student_code = '00000'
                new_student.save()
                new_student.courses.add(course)
                new_student.save()
            return HttpResponseRedirect('/courseList/course/' + course_id)

    return render(request, "CourseEditor/viewCourse.html",
                  {'course': course, 'all_students': Student.objects.all().filter(courses__id=course_id),
                   'suggest_students': Student.objects.all().filter(~Q(courses__id=course_id))})


def add_course(request):
    course = Course()
    course.course_name = "New Course"
    course.course_code = "00000"
    course.save()
    return HttpResponseRedirect('/courseList/editCourse/'+str(course.id))


