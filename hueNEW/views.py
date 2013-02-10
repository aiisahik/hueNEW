# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
import pdb as pdb
import simplejson
import parsepy as ParsePy
import data

def home(request):
	print settings._TEMPLATE_DIRS
	print settings.MEDIA_URL
	print settings.MEDIA_ROOT
	print data.
	# return HttpResponse("Text only, please.", content_type="text/plain")
	return render_to_response('main.html', {'MEDIA_URL':settings.MEDIA_URL})

def graph(request):
	return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL})
