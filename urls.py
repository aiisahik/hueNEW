from django.conf.urls import patterns, include, url
# from django.contrib import admin
# from graph import *
admin.autodiscover()

urlpatterns = patterns('',
	# (r'^$', graph.views.index),
    # url(r'^graph/', graph.views.index),
    url(r'^graph/$', 'hueknew.views.index'),
    # (r'^sitemap\.xml$', 'kinnek.views.sitemapXML'),
    # url(r'^graph/(?P<poll_id>\d+)/$', 'graph.views.detail'),
    # url(r'^graph/(?P<poll_id>\d+)/results/$', 'graph.views.results'),
    # url(r'^graph/(?P<poll_id>\d+)/vote/$', 'graph.views.vote'),
    # url(r'^admin/', include(admin.site.urls)),
)