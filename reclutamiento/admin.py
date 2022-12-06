from django.contrib import admin
from reclutamiento.models import *

class recluta_Admin(admin.ModelAdmin):
	list_filter = ['investigacion', 'documentacion', 'llamadoo', 'saludd', 'estomat', 'municipio']
	list_display = ('nombre', 'ci','llamadoo', 'saludd', 'estomat', 'municipio', 'registrado')
admin.site.register(recluta, recluta_Admin)

class estomatologia_Admin(admin.ModelAdmin):
	pass
admin.site.register(estomatologia, estomatologia_Admin)

class salud_Admin(admin.ModelAdmin):
	pass
admin.site.register(salud, salud_Admin)

class familia_Admin(admin.ModelAdmin):
	pass
admin.site.register(familia, familia_Admin)

class nom_categoria_Admin(admin.ModelAdmin):
	pass
admin.site.register(nom_categoria, nom_categoria_Admin)

class nom_especialidad_Admin(admin.ModelAdmin):
	pass
admin.site.register(nom_especialidad, nom_especialidad_Admin)

class registro_Admin(admin.ModelAdmin):
	pass
admin.site.register(registro, registro_Admin)

class llamado_Admin(admin.ModelAdmin):
	pass
admin.site.register(llamado, llamado_Admin)
