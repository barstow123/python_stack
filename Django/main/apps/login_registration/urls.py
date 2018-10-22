from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index, name='login_index'),
	url(r'^login', views.login, name='login_login'),
	url(r'^register', views.register, name='login_register'),
	url(r'^home', views.home, name='login_home')
] 