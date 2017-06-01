from django.conf.urls import url, include
from . import views
app_name = 'StudentManager'


urlpatterns = [
    url(r'^$', views.index, name='students view'),
    url(r'^(?P<student_id>[\w\-]+)/$', views.edit_student, name='edit student'),

]
