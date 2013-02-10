# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
import pdb as pdb
import simplejson
import parsepy as ParsePy
import data
import requests, json

def home(request):
	print settings._TEMPLATE_DIRS
	print settings.MEDIA_URL
	print settings.MEDIA_ROOT
	# return HttpResponse("Text only, please.", content_type="text/plain")
	
	dateBegin = "2001-10-01T12:00:00.000Z"
	dateEnd = "2013-10-01T12:00:00.000Z"
	api_key = "c9pj47r6q7p7b3gugn5ddb8c"
	api_url = "http://hearst.api.mashery.com/Article/search?"
	api_url += 'limit=200&api_key=c9pj47r6q7p7b3gugn5ddb8c&total=1&start=0&'
	api_url += 'section_id=11561&'
	api_url += 'creation_date_begin='+dateBegin+'&'
	api_url += 'creation_date_end='+dateEnd
	print api_url
	rdata = requests.get(api_url)
	jsonData = json.loads(rdata.text)
	# print rdata.json
	print json.dumps(jsonData, sort_keys=True, indent=4, separators=(',', ': '))
	pdb.set_trace()

	
	return render_to_response('main.html', {'MEDIA_URL':settings.MEDIA_URL})

def graph(request):
	return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL})
