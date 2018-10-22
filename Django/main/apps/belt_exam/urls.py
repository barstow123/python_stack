from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index, name='exam_index'),
	url(r'^login/', views.login, name='exam_login'),
	url(r'^logout/', views.logout, name='exam_logout'),
	url(r'^register/', views.register, name='exam_register'),
	url(r'^dashboard/', views.dashboard, name='exam_dashboard'),
	url(r'^make_job/', views.make_job, name='exam_make_job'),
	url(r'^job/(?P<id>\d+)', views.job_profile, name='exam_job_profile'),
	url(r'^job/edit/(?P<id>\d+)', views.edit_job, name='exam_edit_job'),
	url(r'^job/create/', views.create_job, name='exam_create_job'),
	url(r'^job/destroy/(?P<id>\d+)', views.destroy_job, name='exam_delete_job'),
	url(r'^job/update/(?P<id>\d+)', views.update_job, name='exam_update_job'),
	url(r'^job/add/(?P<id>\d+)', views.add_job, name='exam_add_job'),
	url(r'^job/drop/(?P<id>\d+)', views.drop_job, name='exam_drop_job')
] 