from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index, name='belt_index'),
	url(r'^login/', views.login, name='belt_login'),
	url(r'^register/', views.register, name='belt_register'),
	url(r'^home/', views.home, name='belt_home'),
	url(r'^logout/', views.logout, name='belt_logout'),
	url(r'^review/', views.review, name='belt_review'),
	url(r'^review_post/', views.post_review, name='belt_post_review'),
	url(r'^profile/(?P<id>\d+)', views.profile, name='belt_profile'),
	url(r'^book/(?P<book_id>\d+)', views.book, name='belt_book'),
	url(r'^destroy/(?P<review_id>\d+)', views.destroy, name='belt_delete')
] 