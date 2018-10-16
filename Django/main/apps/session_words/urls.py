from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^add_to_session/$', views.add_to_session),
	url(r'^clear_session/$', views.clear_session)
] 