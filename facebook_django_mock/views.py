from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("¿Que miras, puto?")
def mock(request):
	return JsonResponse({"nara":"naraaa"})