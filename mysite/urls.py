from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'userauth.views.home', name='home'),
	url(r'^login/', include('userauth.urls', namespace='login')),
    url(r'^admin/', include(admin.site.urls)),
	
)
