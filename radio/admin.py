from django.contrib import admin
from radio.models import *

class admin_nom_marca(admin.ModelAdmin):
	pass
admin.site.register(nom_marca, admin_nom_marca)

class admin_unidad_radio(admin.ModelAdmin):
	pass
admin.site.register(unidad_radio, admin_unidad_radio)

class admin_movil(admin.ModelAdmin):
	pass
admin.site.register(movil, admin_movil)


class admin_estaciones_fijas(admin.ModelAdmin):
	pass
admin.site.register(estaciones_fijas, admin_estaciones_fijas)


class admin_estaciones_movil(admin.ModelAdmin):
	pass
admin.site.register(estaciones_movil, admin_estaciones_movil)


class admin_estaciones_portatiles(admin.ModelAdmin):
	pass
admin.site.register(estaciones_portatiles, admin_estaciones_portatiles)


class admin_estaciones_repetidoras(admin.ModelAdmin):
	pass
admin.site.register(estaciones_repetidoras, admin_estaciones_repetidoras)
