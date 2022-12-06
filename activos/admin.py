from django.contrib import admin
from activos.models import *

class submayor_admin(admin.ModelAdmin):
	list_display = ['submayor', 'descripcion']
	list_filter = ['submayor', 'descripcion']

admin.site.register(submayor, submayor_admin)


class articulo_admin(admin.ModelAdmin):
	list_display = ['nombre']
	list_filter = [ 'nombre']

admin.site.register(articulo, articulo_admin)

class grupo_admin(admin.ModelAdmin):
	list_display = ['numero', 'nombre']
	list_filter = ['numero', 'nombre']

admin.site.register(grupo, grupo_admin)

class subgrupos_admin(admin.ModelAdmin):
	list_display = ['numero', 'codigo', 'descripcion']
	list_filter = ['codigo','numero','descripcion']

admin.site.register(subgrupos, subgrupos_admin)


class activos_admin(admin.ModelAdmin):
	list_display = ['subMayor', 'inventario', 'cnmb', 'nombre', 'descripcion',  'dpto',  'importe_activo']
	list_filter = ['subMayor', 'inventario', 'cnmb', 'nombre', 'descripcion',  'dpto',  'importe_activo']

admin.site.register(activos, activos_admin)

class orden_activos_fijos_admin(admin.ModelAdmin):
	list_display = ['fecha', 'activos', 'fecha_alta', 'doc_alta', 'importe',  'fecha_baja',  'doc_baja']
	list_filter = ['fecha', 'activos', 'fecha_alta', 'doc_alta', 'importe',  'fecha_baja',  'doc_baja']

admin.site.register(orden_activos_fijos, orden_activos_fijos_admin)



