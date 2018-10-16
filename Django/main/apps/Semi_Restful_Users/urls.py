from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^show/(?P<id>\d+)', views.show, name='show_user'),
	url(r'^delete/(?P<id>\d+)', views.delete, name='destroy_user'),
	url(r'^edit/(?P<id>\d+)', views.edit, name='edit_user'),
	url(r'^add_user/', views.add_user, name='add_user'),
	url(r'^create_user/', views.create_user, name='create_user'),
	url(r'^update_user/(?P<id>\d+)', views.update_user, name='update_user')
] 