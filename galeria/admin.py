from django.contrib import admin
from galeria.models import *

class categoria_Admin(admin.ModelAdmin):
	pass
admin.site.register(categorias, categoria_Admin)

class imagenes_Admin(admin.ModelAdmin):
	pass
admin.site.register(imagenes, imagenes_Admin)
