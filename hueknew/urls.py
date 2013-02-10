from django.conf.urls import patterns, include, url
# from django.contrib import admin
# import graph
# admin.autodiscover()

urlpatterns = patterns('',
	# (r'^$', graph.views.index),
    url(r'^graph/$', 'graph.views.index'),
)