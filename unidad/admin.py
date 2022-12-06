from django.contrib import admin
from unidad.models import *

class tipo_unidad_organizativa_Admin(admin.ModelAdmin):
	pass
admin.site.register(tipo_unidad_organizativa, tipo_unidad_organizativa_Admin)

class unidad_organizativa_Admin(admin.ModelAdmin):
	pass
admin.site.register(unidad_organizativa, unidad_organizativa_Admin)

class Nom_Tipo_Unidad_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Tipo_Unidad, Nom_Tipo_Unidad_Admin)

class Nom_Perfil_Unidad_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Perfil_Unidad, Nom_Perfil_Unidad_Admin)

class Nom_Provincia_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Provincia, Nom_Provincia_Admin)

class Nom_Municipio_Admin(admin.ModelAdmin):
	list_filter = ('provincia',)
	list_display = ('codigo', 'municipio', 'provincia')
admin.site.register(Nom_Municipio, Nom_Municipio_Admin)

class Nom_Nivel_Unidad_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Nivel_Unidad, Nom_Nivel_Unidad_Admin)

class Unidad_Admin(admin.ModelAdmin):
	search_fields=['nombre']
	list_display = ('codigo', 'nombre', 'municipio', 'subordinacion', 'tipo')
	list_filter = ('municipio', 'tipo')
admin.site.register(Unidad, Unidad_Admin)

class Departamento_Admin(admin.ModelAdmin):
	list_display = ('tipouorganizativa', 'nombre', 'unidad')
	list_filter = ('unidad',)
admin.site.register(Departamento, Departamento_Admin)


class Nom_Plaza_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Plaza, Nom_Plaza_Admin)

class Plaza_Departamento_Admin(admin.ModelAdmin):
	list_display = ('plaza', 'estado', 'departamento')
admin.site.register(Plaza_Departamento, Plaza_Departamento_Admin)


class Nom_Tipo_Plaza_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Tipo_Plaza, Nom_Tipo_Plaza_Admin)
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
