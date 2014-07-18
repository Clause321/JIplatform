from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'index.views.index'),
    # url(r'^JIplatform/', include('JIplatform.JIplatform.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/write/$', 'activity.views.write_news'),
    url(r'^test/$', 'index.views.test'),
    url(r'^news/$', 'activity.views.news'),
    url(r'^news/ac(\d+)/$', 'activity.views.activity_page'),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
   )
