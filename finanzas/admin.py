from django.contrib import admin
from finanzas.models import *

class presupuesto_admin(admin.ModelAdmin):
	pass
admin.site.register(presupuesto, presupuesto_admin)

class nom_partida_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_partida, nom_partida_admin)

