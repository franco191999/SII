from django.contrib import admin
from transporte.models import *


class tipo_admin(admin.ModelAdmin):
	pass 
admin.site.register(tipo, tipo_admin)

class marca_admin(admin.ModelAdmin):
	pass 
admin.site.register(marca, marca_admin)

class estadotecnico_admin(admin.ModelAdmin):
	pass 
admin.site.register(estadotecnico, estadotecnico_admin)

class estadooperativo_admin(admin.ModelAdmin):
	pass 
admin.site.register(estadooperativo, estadooperativo_admin)

class combustible_admin(admin.ModelAdmin):
	pass 
admin.site.register(combustible, combustible_admin)

class demanda_admin(admin.ModelAdmin):
	pass 
admin.site.register(demanda, demanda_admin)

class neumatico_admin(admin.ModelAdmin):
	pass 
admin.site.register(neumatico, neumatico_admin)

class bateria_admin(admin.ModelAdmin):
	pass 
admin.site.register(bateria, bateria_admin)

class funcion_admin(admin.ModelAdmin):
	pass 
admin.site.register(funcion, funcion_admin)

class parque_admin(admin.ModelAdmin):
	list_display=('matricula', 'unidad', 'tipo', 'marca', 'modelo', 'serie', 'motor', 'estadotecnico', 'estadooperativo', 'combustible', 'neumatico', 'bateria')
	list_filter=['estadotecnico', 'estadooperativo', 'funcion', 'combustible', 'tipo', 'demanda', 'unidad']
	list_per_page=300
	search_fields = ['matricula']

admin.site.register(parque, parque_admin)

