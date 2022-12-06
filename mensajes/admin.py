from django.contrib import admin
from mensajes.models import *


class categoria_admin(admin.ModelAdmin):
	pass
admin.site.register(categoria, categoria_admin)

class mensaje_admin(admin.ModelAdmin):
	pass
admin.site.register(mensaje, mensaje_admin)

class eliminar_destinatario_admin(admin.ModelAdmin):
	pass
admin.site.register(eliminar_destinatario, eliminar_destinatario_admin)

class mensaje_leido_admin(admin.ModelAdmin):
	pass
admin.site.register(mensaje_leido, mensaje_leido_admin)
