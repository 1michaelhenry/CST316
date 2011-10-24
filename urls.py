from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstBlog.views.home', name='home'),
    # url(r'^FirstBlog/', include('FirstBlog.foo.urls')),
    url(r'^$', 'CST316.blog.views.home', name='home'),
    url(r'^login', 'CST316.blog.views.login', name='login'),
    url(r'^auth', 'CST316.blog.views.auth', name='auth'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
