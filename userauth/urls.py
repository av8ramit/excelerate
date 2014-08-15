from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^register/$', 'userauth.views.register', name='register'),
		url(r'^auth/$', 'userauth.views.login', name='login'),
		url(r'^sendregister/$', 'userauth.views.send', name='send'),
		)

