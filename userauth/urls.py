from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^$', 'userauth.views.home', name='front'),
		url(r'^register/$', 'userauth.views.register', name='register'),
		url(r'^auth/$', 'userauth.views.login', name='auth'),
		url(r'^sendregister/$', 'userauth.views.send', name='send'),
		url(r'^sendregister/postregister/$', 'userauth.views.postregister', name='send_post'),
		)

