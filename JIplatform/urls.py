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
    url(r'^write/$', 'activity.views.write_act'),
    url(r'^test/$', 'index.views.test'),
    url(r'^news/$', 'activity.views.activity', {'typeOrGroup': 'type', 'name': 'news'}),
    url(r'^activity/$', 'activity.views.activity', {'typeOrGroup': 'type', 'name': 'activity'}),
    url(r'^announce/$', 'activity.views.activity', {'typeOrGroup': 'type', 'name': 'announce'}),
    url(r'^group/(?P<name>[a-zA-Z]+)/$', 'activity.views.activity', {'typeOrGroup': 'group'}),
    url(r'^ac/(\d+)/$', 'activity.views.activity_page'),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^group/$', 'group.views.group'),
    url(r'^register/$', 'user_ctrl.views.register'),
    url(r'^login/$', 'user_ctrl.views.login_view'),
    url(r'^logout/$', 'user_ctrl.views.logout_view'),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
   )
