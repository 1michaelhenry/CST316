from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstBlog.views.home', name='home'),
    # url(r'^FirstBlog/', include('FirstBlog.foo.urls')),
    url(r'^$', 'CST316.blog.views.home', name='home'),
    url(r'^authorize', 'CST316.blog.views.authorize', name='authorize'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
    url(r'^test.html$', 'CST316.blog.views.test', name='test'),
    url(r'^postblog$', 'CST316.blog.views.postblog', name='postblog'),
    url(r'^loginerror$', 'CST316.blog.views.loginerror', name='loginerror'),
    url(r'^logout', 'CST316.blog.views.logout', name='logout'),
    url(r'^previewblog$', 'CST316.blog.views.previewblog', name='previewblog'),
    url(r'^cancelpost$', 'CST316.blog.views.cancelpost', name='cancelpost'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)),
)

from CST316 import settings
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^css/(?P<path>.*)$', 'django.views.static.serve',
		 {'document_root' : settings.MEDIA_ROOT}),
		)

