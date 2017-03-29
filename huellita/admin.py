from django.contrib import admin

from .models import Registrado, Contacto

from .forms import RegModelForm

class AdminRegistrado(admin.ModelAdmin):
	form = RegModelForm 		#Mostramos el formulario RegModelForm en el site
	list_display = ['email', 'nombre', 'dni', 'timestamp', ]
	list_filter = ['timestamp', ]
	list_editable = ['nombre', ]
	search_fields = ['email', 'nombre', ]

	#class Meta:
	#	model = Registrado


class AdminContacto(admin.ModelAdmin):
	list_display = ['email', 'nombre', 'mensaje', 'timestamp', ]
	list_filter = ['timestamp', ]
	list_editable = ['nombre', ]
	search_fields = ['email', 'nombre', ]

	class Meta:
		model = Contacto


admin.site.register(Registrado, AdminRegistrado)
admin.site.register(Contacto , AdminContacto)


