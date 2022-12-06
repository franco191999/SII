from django.contrib import admin
from carpeta.models import *

class Categoria_Admin(admin.ModelAdmin):
	pass
admin.site.register(Categoria, Categoria_Admin)

class Ficheros_Admin(admin.ModelAdmin):
	pass
admin.site.register(Ficheros, Ficheros_Admin)

class Objetivo_Admin(admin.ModelAdmin):
	pass
admin.site.register(Objetivo, Objetivo_Admin)

class Tipo_web_Admin(admin.ModelAdmin):
	pass
admin.site.register(Tipo_web, Tipo_web_Admin)

class Ancho_banda_Admin(admin.ModelAdmin):
	pass
admin.site.register(Ancho_banda, Ancho_banda_Admin)

class Anno_unidad_Admin(admin.ModelAdmin):
	pass
admin.site.register(Anno_unidad, Anno_unidad_Admin)

class Resultados_Admin(admin.ModelAdmin):
	pass
admin.site.register(Resultados, Resultados_Admin)

class Conectividad_Admin(admin.ModelAdmin):
	pass
admin.site.register(Conectividad, Conectividad_Admin)

class P_web_Admin(admin.ModelAdmin):
	pass
admin.site.register(P_web, P_web_Admin)

class Enlaces_Admin(admin.ModelAdmin):
	pass
admin.site.register(Enlaces, Enlaces_Admin)

class Aplicaciones_Admin(admin.ModelAdmin):
	pass
admin.site.register(Aplicaciones, Aplicaciones_Admin)

class Documentos_Admin(admin.ModelAdmin):
	list_filter = ("unidad",)
	list_display = ("id","unidad","documento","ficheros")
admin.site.register(Documentos, Documentos_Admin)


# Register your models here.
