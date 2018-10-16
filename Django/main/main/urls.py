from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^semi_restful_users/', include('apps.Semi_Restful_Users.urls')),
	url(r'^ninja_gold/', include('apps.ninja_gold.urls')),
	url(r'^session_words/', include('apps.session_words.urls')),
	url(r'^surveys/', include('apps.surveys.urls')),
    url(r'^random_word_generator/', include('apps.random_word_generator.urls')),
	url(r'^first_app/', include('apps.first_app.urls')), # And now we use the include function to pull in our first_app.urls...
	url(r'^time_display/', include('apps.time_display.urls')),
	url(r'^admin/', admin.site.urls)
]