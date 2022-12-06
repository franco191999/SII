from django.contrib import admin
from presupuesto.models import *
# Register your models here.
class Presupuesto_Unidad_Admin(admin.ModelAdmin):
	list_display=["cantidad_inicial", "cantidad_actual", "unidad", "actualizacion"]
	list_filter=["actualizacion"]
admin.site.register(Presupuesto_Unidad, Presupuesto_Unidad_Admin)

class Orden_Servicio_Unidad_Admin(admin.ModelAdmin):
	list_display=("numero", "importe", "unidad", "tipo_servicio", "actualizacion")
	list_filter=["actualizacion"]
admin.site.register(Orden_Servicio_Unidad, Orden_Servicio_Unidad_Admin)

