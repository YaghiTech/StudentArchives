from django.conf.urls import url

from . import views

app_name = 'CourseEditor'


urlpatterns = [
    #url(r'^', views.index, name="index"),
    url(r'^$',views.index, name='course view'),
    url(r'^course/(?P<course_id>[\w\-]+)/$', views.edit_course, name='edit course'),

    url(r'^addCourse/', views.add_course, name='addcourse'),

]