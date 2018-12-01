from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
import time

import json

# Default logger
logger = logging.getLogger(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logger.handlers = gunicorn_logger.handlers
    logger.setLevel(gunicorn_logger.level)

# Create your views here.
def index(request):
	template = loader.get_template('app/index.html')
	return HttpResponse(template.render({}, request))
@csrf_exempt
def mock(request):
	checkId = time.time()
	if(request.method == 'GET'):
		queryParams = request.GET
		logger.info(queryParams)
		
		if len(queryParams.keys()) > 0:
			logger.info("token de validacion: " + str(queryParams.get("hub.verify_token")))
			checkId = queryParams.get("hub.challenge")
	else:
		queryParams = request.POST
		strJson = request.body.decode('utf-8')
		logger.info(queryParams)
		logger.info(strJson)
		if len(strJson) > 0:
			data = json.loads(strJson)
			logger.info(data)
	return HttpResponse(checkId)