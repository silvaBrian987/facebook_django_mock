from django.db import models

# Create your models here.
"""
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
"""
class Caballero(models.Model):
	"""
		Caballeril clase que representa un caballero (aka. puto)
	"""
	nombre = models.CharField(max_length=50)
	puto = models.IntegerField(default=0)
class Configuracion(models.Model):
	"""
		Modelo de configuracion por clave-valor
	"""
	clave = models.CharField(max_length=100)
	valor = models.CharField(max_length=100)