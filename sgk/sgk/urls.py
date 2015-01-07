# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sgk import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('frontend.urls')),
    # url(r'^sgk/', include('sgk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )