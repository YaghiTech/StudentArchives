from django.shortcuts import render, HttpResponseRedirect
from CourseEditor.models import Student
import calendar
import datetime

# Create your views here.
def index(request):
    all_students = Student.objects.all()
    if request.method == 'POST':
        for student in all_students:
            if request.POST.get('edit'+str(student.id)):
                return HttpResponseRedirect('/studentList/' + str(student.id))
    return render(request, "StudentManager/index.html", {'all_students' : all_students})


def edit_student(request,student_id):
    student = Student.objects.get(id=student_id)

    old_year = datetime.datetime.now().year-40
    test = ''
    months = []
    for i in range(1, 13):
        months.append((i, calendar.month_name[i]))
    if request.method == 'POST':
        for name in Student.student_field_names:
            request_text = request.POST.get(name, None)
            if request_text is not None and request_text is not '':
                setattr(student, name, request_text)
                student.save()

            student.student_age = student.student_age.replace(year=int(request.POST.get('student_age_year', None))+old_year,
                                                              day=int(request.POST.get('student_age_day', None)),
                                                              month=int(request.POST.get('student_age_month', None))+1)
            student.save()
    return render(request, "StudentManager/editStudent.html", {'student':student,'months':months,'current_year':old_year,'test':test})

