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

JSONDATA = ""

def home(request):
	iterate('2011-10-01T12:00:00.000Z')
	# print JSONDATA
	global JSONDATA
	JSONDATA = "["+JSONDATA+"]"
	jsonObj = json.loads(JSONDATA)

	# print JSONDATA
	# pdb.set_trace()
	# jsonDD = jsonObj.stringify(testObject);
	jsonDD = json.dumps(jsonObj)
	return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL, 'jsonData':jsonDD})
	# return render_to_response('main.html', {'MEDIA_URL':settings.MEDIA_URL})

	# iterate('2010-09-01T12:00:00.000Z')


def iterate(dateEnd):
	# runway = json.load(f)
	keywords = "runway"
	limit = "10"
	runway = hearstAPI('11561',dateEnd,keywords,limit)
	count = runway['count']
	print dateEnd
	
	i = 0
	for x in runway['items']:
		url = x['canonical_url']
		title = x['meta_title']
		# print json.dumps(x, sort_keys=True, indent=4, separators=(',', ': '))
		domain = x["origin_site_url"]
		    # creation = x["creation_date"]
		date = x['publish_date']
		if "pages" in x:
			# print image["large_url"]
			# print json.dumps(x['pages'], sort_keys=True, indent=4, separators=(',', ': '))
			for page in x["pages"]:
				if "imagelist" in page:
					# print json.dumps(page["imagelist"], sort_keys=True, indent=4, separators=(',', ': '))
					for image in page["imagelist"]:
						imageURL = domain + image["default_url"]
						# print x['publish_date'] + " | " + url + "| " + title + "|" + date
						imagedict = {'imageURL':imageURL, 
							'date':date, 
							'title':title,
							'url':url,
							'imageURL':imageURL}
						# jsonOBJ =+ json.dumps(imagedict, sort_keys=True, indent=4, separators=(',', ': '))
						# print json.dumps(imagedict)
						global JSONDATA
						jsonStr = json.dumps(imagedict)
						# JSONDATA = JSONDATA.append(jsonStr)
						if JSONDATA == "":
							JSONDATA = jsonStr
						else: 
							JSONDATA = JSONDATA + ","+jsonStr
						# jsonOBJ[i] = jsonOBJ.append(jsonData)
						i += 1
						# pdb.set_trace()
						# print JSONDATA
				# print json.dumps(x['pages'], sort_keys=True, indent=4, separators=(',', ': '))

	
	print "new dateEnd: " + dateEnd + ", count: " + str(count)
	if count == 0:
		# no more! 
		# JSONDATA = "["+JSONDATA + "]"
		return JSONDATA
		# return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL, 'jsonData':JSONDATA})
	elif dateEnd < "2005-10-01T12:00:00.000Z":
		# print JSONDATA
		# JSONDATA = "["+JSONDATA + "]"
		if not JSONDATA == None:
			return JSONDATA
		# return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL, 'jsonData':JSONDATA})
	else: 
		dateEnd = runway['items'][count-1]['publish_date']
		iterate(dateEnd)


def hearstAPI(section_id,dateEnd,keywords,limit):
	# print settings._TEMPLATE_DIRS
	# print settings.MEDIA_URL
	# print settings.MEDIA_ROOT
	# return HttpResponse("Text only, please.", content_type="text/plain")
	
	dateBegin = "2001-10-01T12:00:00.000Z"
	# dateEnd = "2013-10-01T12:00:00.000Z"
	api_key = "c9pj47r6q7p7b3gugn5ddb8c"
	api_url = "http://hearst.api.mashery.com/Article/search?"
	api_url += "_version=2&"
	api_url += "_pretty=1&"
	api_url += 'keywords='+keywords+'&'
	api_url += 'limit='+limit+'&'
	api_url += 'api_key=c9pj47r6q7p7b3gugn5ddb8c&total=1&start=0&'
	# api_url += "_json={%22article_section_id%22:[11561,11562,11563,11564,11565]}&"
	# api_url += "article_section_id=8774&"
	api_url += 'pages=full&'
	api_url += 'site_id=584&'
	# api_url += 'article_section_id='+section_id+'&'
	api_url += 'creation_date_begin='+dateBegin+'&'
	api_url += 'creation_date_end='+dateEnd
	# print api_url
	rdata = requests.get(api_url)
	x = json.loads(rdata.text)
	return x

	# # print rdata.json
	# print json.dumps(jsonData, sort_keys=True, indent=4, separators=(',', ': '))
	# # pdb.set_trace()
	# return render_to_response('main.html', {'MEDIA_URL':settings.MEDIA_URL})



def graph(request):
	return render_to_response('graph.html', {'MEDIA_URL':settings.MEDIA_URL})
