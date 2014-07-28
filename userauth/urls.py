from django.conf.urls import patterns, url

from userauth import views

urlpatterns = patterns('', 
		url(r'^$', views.home, name='home')
		url(r'^/register/$', views.register, name='register')
		url(r'^/login/$', views.login, name='login')
		)

