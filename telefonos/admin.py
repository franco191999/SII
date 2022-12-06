from django.contrib import admin
from telefonos.models import *

class Pizarra_Admin(admin.ModelAdmin):
	pass
admin.site.register(Pizarra, Pizarra_Admin)


class Telefono_Fijo_Admin(admin.ModelAdmin):
	pass
admin.site.register(Telefono_Fijo, Telefono_Fijo_Admin)


class Extencion_Admin(admin.ModelAdmin):
	pass
admin.site.register(Extencion, Extencion_Admin)
