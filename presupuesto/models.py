#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.db import models
from unidad.models import Unidad

#áéíóú

tipo_servicio = (
    ('compra', 'Compra'),
    ('mantenimiento', 'Mantenimiento'),
    ('dictamen', 'Dictamen Técnico'),
    ('reparacion', 'Reparación'),
    ('montaje', 'Montaje'),
    ('modernizacion', 'Modernización'),
)

directorio_fotografias = '%s/%s'


class Presupuesto_Unidad(models.Model):
	cantidad_inicial = models.FloatField('Presupuesto Inicial de Unidad', blank=True, null=False)
	cantidad_actual = models.FloatField('Presupuesto Actual de Unidad', blank=True, null=False)
	unidad = models.ForeignKey(Unidad, max_length = 256, blank=True, on_delete=models.CASCADE)
	actualizacion = models.DateField(Unidad,  auto_now_add=True)


	def __str__(self):
		return '%s' % (self.cantidad_actual)

class Orden_Servicio_Unidad(models.Model):
	numero = models.CharField('Número de Orden', max_length = 5, blank=True, null=True)
	tipo_servicio = models.CharField('Tipo', blank=False, max_length=256, null=True,choices=tipo_servicio)
	descripcion = models.TextField('Descripción', max_length = 256, blank=True, null=True)
	importe = models.FloatField('Importe', blank=True, null=False)
	unidad = models.ForeignKey(Unidad, max_length = 256, blank=True, on_delete=models.CASCADE)
	actualizacion = models.DateField(Unidad, auto_now_add=True)

	def __str__(self):
		return '%s' % (self.numero)





