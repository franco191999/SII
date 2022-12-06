from django.contrib import admin
from inspeccion.models import *

class Nom_Estado_Deficiencia_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Estado_Deficiencia, Nom_Estado_Deficiencia_Admin)

class Nom_Aspecto_Deficiencia_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Aspecto_Deficiencia, Nom_Aspecto_Deficiencia_Admin)

class Nom_Tipo_Visita_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Tipo_Visita, Nom_Tipo_Visita_Admin)

class Visita_Admin(admin.ModelAdmin):

	search_fields=['unidad', 'fecha']

	list_filter=['visitado']

	list_per_page=10

admin.site.register(Visita, Visita_Admin)

class Deficiencia_Admin(admin.ModelAdmin):

	search_fields=['visita', 'aspecto']

	list_filter=['puntoaspecto']

	list_per_page=10

admin.site.register(Deficiencia, Deficiencia_Admin)
