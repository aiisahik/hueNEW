# Create your views here.

import django.template
from django.conf import settings
import pdb as pdb
import simplejson

def index(request):
	return render_to_response('/templates/main.html', {'poll': p})
