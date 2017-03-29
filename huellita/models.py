from __future__ import unicode_literals

from django.db import models


#blank admite el apellido en blnaco en el formulario y null admite el apellido en blanco para la base de datos
class Registrado(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255, blank=True, null=True)
	dni = models.IntegerField()
	telefono = models.IntegerField()
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	
	def __unicode__(self): #Python 2
		return self.email

	def __str__(self): #Python 3
		return self.email


class Contacto(models.Model):
	nombre = models.CharField(max_length=255)
	email = models.EmailField()
	mensaje = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	
	def __unicode__(self): #Python 2
		return self.email

	def __str__(self): #Python 3
		return self.email
