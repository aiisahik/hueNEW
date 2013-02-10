from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
import pdb as pdb
import simplejson
import parsepy as ParsePy

ParsePy.APPLICATION_ID = "myIUqBxrUgSfoQSQeuhM09gt9GBa5cpVKqQ34H1Z"
ParsePy.MASTER_KEY = "YwjOgW8LC0anLsag1j50h57ulDWGsaP2aRLeMjmw"

def save(request, json):
	hueData = ParsePy.ParseObject("hue")
	hueData.color = 1337
	hueData.articleURL = ""
	hueData.imageURL = ""
	hueData.save()
	return hueData

def getData(request,id):
	# SEE: https://github.com/pktck/ParsePy
	hueData = ParsePy.ParseQuery("hue").get(id)
	# // or 
	query = ParsePy.ParseQuery("hue")
	query = query.lt("color", 200).gt("color", 100)
	hueDataCollection = query.fetch()
	return hueDataCollection