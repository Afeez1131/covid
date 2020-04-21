from django.shortcuts import render, redirect
from .models import Covid
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	# 
	import requests
	import json
	#pk = 'pk_c1d58b331e2e46f3a0f0a55dc5b1044c'
	#return the json of all countries including slug
	'''{'Country': 'Nigeria', 'Slug': 'nigeria', 'ISO2': 'NG'}'''
	api_request = requests.get('https://api.covid19api.com/countries')

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = 'Error'
	
	# covid.country = api[0]['Country']
	# covid.slug = api[0]['Slug']
	# covid.save()
	
	return render(request, 'home.html', {'api': api,
		})


def details(request, slug):
	import requests
	import json

	api_request = requests.get("https://api.covid19api.com/dayone/country/" + slug)

	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = 'Error'
		
	return render(request, 'details.html', {'api': api,
		})

def confirmed(request, slug):
	import requests
	import json

	api_request = requests.get("https://api.covid19api.com/live/country/" + slug + "/status/confirmed")
	try:
		confirm = json.loads(api_request.content)
	except Exception as e:
		confirm = 'Error'

	return render(request, 'home.html', {'confirm': confirm})