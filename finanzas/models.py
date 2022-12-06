import datetime
from django.db import models
from unidad.models import *
from django.contrib import admin
class nom_partida(models.Model):
	partida = models.CharField('Partida', max_length=25, blank=False, null=False)
	descripcion = models.TextField('Descripcion', max_length=256, blank=True, null=False)
	def __str__(self):
		return '%s' % (self.partida)

class presupuesto (models.Model):
	unidad = models.OneToOneField(Unidad, on_delete=models.CASCADE)
	monto_inicial = models.FloatField('Presupuesto asignado', max_length = 256, blank=True, null=True)
	fecha = models.DateField('Fecha del Retiro', auto_now_add=True)

	#El problema con el saldo es que tiene que obtenerse mediante consultas especificas. De este modo no funciona, porq
	#te da la opcion de modificarlo manualmente
	#saldo = models.FloatField('Saldo', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.unidad.nombre)

class retiros (models.Model):
	unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
	factura = models.CharField('Numero de factura', max_length=25, blank=False, null=False)
	partida = models.ForeignKey(nom_partida, on_delete=models.CASCADE)
	importe = models.FloatField('Importe a Pagar', max_length = 256, blank=False, null=False)
	detalles = models.TextField(max_length=256, blank=True, null=True)
	fecha = models.DateField('Fecha del Retiro', auto_now_add=True)

class retirosAdmin(admin.ModelAdmin):
	list_display = ('unidad', 'factura', 'partida', 'importe', 'fecha')
admin.site.register(retiros, retirosAdmin)
