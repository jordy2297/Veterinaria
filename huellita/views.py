from django.conf import settings       #Importamos settings
from django.core.mail import send_mail #Importamos modulo para gmail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado, Contacto


def inicio(request):
	cabezera = "Huellitas K&S"
	titulo = "Veterinaria Huellitas K&S"

	if request.user.is_authenticated():
		titulo = "%s" %(request.user)

	form = RegModelForm(request.POST or None)

	context = {
		"cabezera": cabezera,
		"titulo": titulo,
		"form": form,
	}

	if form.is_valid():

		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		apellido = form.cleaned_data.get("apellido")
		email = form.cleaned_data.get("email")
		dni = form.cleaned_data.get("dni")
		telefono = form.cleaned_data.get("telefono")
		#Modificaciones antes de guardar
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

	#Personalizamos para superusuarios
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp")#filter(nombre__icontains="jordy")

		context = {
			"queryset": queryset,
		}
		#print instance
		#print instance.timestamp

		#form_data = form.cleaned_data
		#nombre = form_data.get("nombre")
		#email = form_data.get("email")
		#obj = Registrado.objects.create(nombre=nombre, apellido=apellido, email=email, dni=dni, telefono=telefono)
	
	return render(request, "inicio.html", context)

def contact(request):
	cabezera = "Huellitas K&S"
	titulo = "Contactanos"

	form = ContactForm(request.POST or None)

	context = {
		"cabezera": cabezera,
		"titulo": titulo,
		"form": form,
	}

	if form.is_valid():

		#for key, value in form.cleaned_data.iteritems():
		#	print key, value
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		mensaje = form.cleaned_data.get("mensaje")
		'''
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "francoperez2297@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(
			asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False    #Para que nos salgan los mensajes de errores
			)
		'''
		context = {
			"titulo": "Gracias por contactarnos!"
		}

	return render(request, "forms.html", context)