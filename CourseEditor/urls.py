from django.conf.urls import url

from . import views

app_name = 'CourseEditor'


urlpatterns = [
    url(r'^editCourse/(?P<course_code>[\w\-]+)/$', views.index, name='edit course'),
    url(r'^addCourse', views.addCourse, name='add course'),

]