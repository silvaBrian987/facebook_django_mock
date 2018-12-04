# DJANGO PACKAGES
from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# PYTHON PACKAGES
import logging
import time
import os

# THIRD PARTY PACKAGES
import facebook
import json
import requests

# LOCAL PACKAGES
from .models import Caballero
from .models import Configuracion

# Default logger
logger = logging.getLogger(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    print(gunicorn_logger)
    logger.handlers = gunicorn_logger.handlers
    if os.environ.get('DJANGO_SERVER') == "True":
    	logger.setLevel('INFO')
    else:
    	logger.setLevel(gunicorn_logger.level)
    print(logger)

# Create your views here.
def index(request):
	template = loader.get_template('app/index.html')
	return HttpResponse(template.render({}, request))
@csrf_exempt
def handle_webhook_call(request):
	authToken = manage_webhook_authentication(request)
	if authToken != "":
		return HttpResponse(authToken)
	return HttpResponse("")
def caballero(request):
	caballeros = Caballero.objects.all()
	arrCaballeros = []
	for caballero in caballeros:
		arrCaballeros.append({"nombre":caballero.nombre, "puto":caballero.puto})
	return JsonResponse(arrCaballeros, safe=False)
def loginFB(request):
	app_id = Configuracion.objects.get(clave='facebook.app.id').valor
	app_secret = Configuracion.objects.get(clave='facebook.app.secret').valor

	if "code" in request.GET:
		redirect_uri = "https://" + request.get_host() + request.path
		logger.info("redirect_uri=" + redirect_uri)
		payload = {'client_id' : app_id, 'redirect_uri' : redirect_uri, 'client_secret' : app_secret, 'code' : request.GET['code']}
		fb_response = requests.get('https://graph.facebook.com/v3.2/oauth/access_token', params=payload, verify=False)
		logger.info(fb_response)
		logger.info(fb_response.text)
		#return 
	else:
		logger.info("wachin")
	
	access_token = app_id + "|" + app_secret
	logger.info(access_token)
	graph = facebook.GraphAPI(version="3.1")
	perms = ["manage_pages","publish_pages"]
	return JsonResponse({'loginURL' : graph.get_auth_url(app_id, 'https://nginx-marine.193b.starter-ca-central-1.openshiftapps.com/mock/', perms)})
def getAppData(request):
	access_token = ""
	if "access_token" in request.session:
		access_token = request.session["access_token"]
	elif "access_token" in request.GET:
		access_token = request.GET["access_token"]
	else:
		app_id = Configuracion.objects.get(clave='facebook.app.id').valor
		app_secret = Configuracion.objects.get(clave='facebook.app.secret').valor
		access_token = app_id + "|" + app_secret
	print("access_token=" + access_token)
	graph = facebook.GraphAPI(access_token=access_token, version="3.1")
	return JsonResponse(graph.get_object(id="me"), safe=False)
def handle_webhook_authentication(request):
	"""Metodo para devolver autorizacion de login para Facebook Webhooks"""
	#logger.info("token de validacion: " + str(queryParams.get("hub.verify_token")))
	challenge = ""
	if request.method == 'GET':
		if "hub.challenge" in request.GET:
			challenge = request.GET["hub.challenge"]
	elif request.method == 'POST':
		strJson = request.body.decode('utf-8')
		if len(strJson) > 0:
			data = json.loads(strJson)
			if "hub.challenge" in data:
				challenge = data["hub.challenge"]
	return challenge