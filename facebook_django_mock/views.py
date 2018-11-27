from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponse

import time

# Create your views here.
def index(request):
	template = loader.get_template('app/index.html')
	return HttpResponse(template.render({}, request))
def mock(request):
	queryParams = request.GET
	print(queryParams)
	checkId = time.time()
	if len(queryParams.keys()) > 0:
		print("token de validacion: " + str(queryParams.get("hub.verify_token")))
		checkId = queryParams.get("hub.challenge")
	return JsonResponse(checkId)