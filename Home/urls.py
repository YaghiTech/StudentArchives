from django.conf.urls import url ,include

from . import views

app_name = 'Home'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include('CourseEditor.urls')),
]

