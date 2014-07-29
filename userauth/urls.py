from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^$', 'userauth.views.home', name='home'),
		url(r'^register/$', 'userauth.views.register', name='register'),
		url(r'^login/$', 'userauth.views.login', name='login'),
		)

