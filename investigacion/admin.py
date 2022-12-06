from django.contrib import admin
from investigacion.models import *

# Register your models here.

class tipo_publicacion_admin(admin.ModelAdmin):
	pass
admin.site.register(tipo_publicacion, tipo_publicacion_admin)

class publicacion_admin(admin.ModelAdmin):
	pass
admin.site.register(publicaciones, publicacion_admin)




class nom_lineamiento_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_lineamiento, nom_lineamiento_admin)


class nom_estado_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_estado, nom_estado_admin)


class nom_clasificacion_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_clasificacion, nom_clasificacion_admin)


class nom_tipo_salida_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_tipo_salida, nom_tipo_salida_admin)


class nom_categ_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_categ, nom_categ_admin)


class nom_tipo_proyecto_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_tipo_proyecto, nom_tipo_proyecto_admin)


class nom_impacto_admin(admin.ModelAdmin):
	pass
admin.site.register(nom_impacto, nom_impacto_admin)


class proyectos_admin(admin.ModelAdmin):
	pass
admin.site.register(proyectos, proyectos_admin)
