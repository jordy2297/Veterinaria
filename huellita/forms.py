#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms

from .models import Registrado, Contacto

class RegModelForm(forms.ModelForm):
	class Meta:		
		model = Registrado		#Usamos el Modelo Regustrado para el formulario
		fields = ["nombre", "apellido", "dni", "telefono", "email", ]		#Elegimos los campos del modelo para que se muestren en el formulario

	def clean_email(self):
		email = self.cleaned_data.get("email")
		#split nos permite separa el texto que sigue de lo indicado entre comillas
		#email_base, proveedor = email.split("@")
		#dominio, extension = proveedor.split(".")
		proveedor = email[-9:]
		
		if not proveedor == "gmail.com":
			raise forms.ValidationError("Por favor utiliza una direccion de tipo: nombre@gmail.com")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		
		if not nombre.isalpha():
			raise forms.ValidationError("El nombre no debe contener números")
		return nombre

	def clean_apellido(self):
		apellido = self.cleaned_data.get("apellido")
		
		if not apellido.isalpha():
			raise forms.ValidationError("El apellido no debe contener números")
		return apellido

	def clean_telefono(self):
		telefono = self.cleaned_data.get("telefono")
		telf = str(telefono)

		if len(telf) < 9 or len(telf) > 9:
			raise forms.ValidationError("El telefono debe contener 9 digitos")
		return telefono
	
	def clean_dni(self):
		dni = self.cleaned_data.get("dni")
		d = str(dni)
		
		if len(d) < 8 or len(d) > 8:
			raise forms.ValidationError("El dni debe contener 8 digitos")
		return dni 


class ContactForm(forms.Form):
	nombre = forms.CharField()
	email = forms.CharField()
	mensaje = forms.CharField(widget=forms.Textarea)

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		
		if not nombre.isalpha():
			raise forms.ValidationError("El nombre no debe contener números")
		return nombre

	def clean_email(self):
		email = self.cleaned_data.get("email")

		proveedor = email[-9:]
		
		if not proveedor == "gmail.com":
			raise forms.ValidationError("Por favor utiliza una direccion de tipo: nombre@gmail.com")
		return email

	def clean_mensaje(self):
		mensaje = self.cleaned_data.get("mensaje")

		if len(mensaje) > 400:
			raise forms.ValidationError("El mensaje no debe exceder de los 400 caracteres")
		return mensaje