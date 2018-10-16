from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	url(r'^(?P<num>\d)$', views.number),
	url(r'^(?P<num>\d)/edit$', views.editBlogNum),
	url(r'^(?P<num>\d)/delete$', views.destroy)
]                            # anticipation of all the routes that will be coming soon