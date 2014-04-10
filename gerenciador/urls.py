from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gerenciador.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^all_events/', 'gerenciador.views.all_events', name='all_events'),
)

from django.conf import settings

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
		    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
			    {'document_root': settings.MEDIA_ROOT}))
