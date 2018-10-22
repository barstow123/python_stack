from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index, name='course_index'),
	url(r'^destroy/(?P<id>\d+)', views.destroy, name='delete_course'),
	url(r'^create/', views.create, name='add_course')
] 