#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from distribucion.models import  *


class tipomovimiento_admin(admin.ModelAdmin):
	pass 
admin.site.register(tipomovimiento, tipomovimiento_admin)


class mesa_admin(admin.ModelAdmin):
	pass 
admin.site.register(mesa, mesa_admin)

class movimiento_admin(admin.ModelAdmin):
	list_display = ("tipomovimiento", "unidad", "cantidad", "importe", "actualizacion") 
	list_filter = ("tipomovimiento",) 
admin.site.register(movimiento, movimiento_admin)

