from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index, name='wall_index'),
	url(r'^login', views.login, name='wall_login'),
	url(r'^register', views.register, name='wall_register'),
	url(r'^home', views.home, name='wall_home'),
	url(r'^logout/', views.logout, name='wall_logout'),
	url(r'^post/', views.post, name='wall_post'),
	url(r'^comment/', views.comment, name='wall_comment')
] 