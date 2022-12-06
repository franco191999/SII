from django.contrib import admin
from tareas.models import *


class Nom_Categoria_Tarea_admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Categoria_Tarea, Nom_Categoria_Tarea_admin)


class Nom_Clasificacion_Tarea_admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Clasificacion_Tarea, Nom_Clasificacion_Tarea_admin)


class Nom_Prioridad_Tarea_admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Prioridad_Tarea, Nom_Prioridad_Tarea_admin)


class Nom_Estado_Tarea_admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Estado_Tarea, Nom_Estado_Tarea_admin)

class Tarea_admin(admin.ModelAdmin):

        list_filter=['responsable','participantes',]

admin.site.register(Tarea, Tarea_admin)
