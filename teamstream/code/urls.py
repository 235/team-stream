from django.conf.urls.defaults import * #IGNORE:W0614 - need to import everything, django Ticket #5350
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.root),
    
    url(r'^teamstream/', include('apps.teamstream.urls')),
    
    url(r'^$', 'apps.teamstream.views.main', name='main'),
    url(r'^report/$', include('apps.teamstream.report_urls')),
)

if settings.DEBUG:
    media_root = hasattr(settings, 'MEDIA_ROOT') and settings.MEDIA_ROOT or '/media/'
    static_root = hasattr(settings,'STATIC_ROOT') and settings.STATIC_ROOT or '/static/'
    admin_root = hasattr(settings,'ADMIN_MEDIA_ROOT') and settings.ADMIN_MEDIA_ROOT or '/media-admin/'    
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_root}),  
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static_root}), 
        (r'^media-admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': admin_root}),         
    )
