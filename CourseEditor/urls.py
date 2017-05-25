from django.conf.urls import url

from . import views

app_name = 'CourseEditor'


urlpatterns = [
    #url(r'^', views.index, name="index"),
    url(r'^$',views.index, name='course view'),
    url(r'^course/(?P<course_id>[\w\-]+)/$', views.view_course, name='view course'),
    url(r'^course/(?P<course_id>[\w\-]+)/addStudent', views.add_student, name='add student'),

    url(r'^editCourse/(?P<course_id>[\w\-]+)/$', views.edit_course, name='edit course'),

    url(r'^addCourse/', views.add_course, name='add course'),

]