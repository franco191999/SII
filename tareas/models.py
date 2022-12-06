import datetime
from django.db import models
from rrhh.models import *


class Nom_Categoria_Tarea(models.Model):
	categoria = models.CharField('Tipo de Tarea', max_length=256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.categoria)


class Nom_Clasificacion_Tarea(models.Model):
	clasificacion = models.CharField('Tipo de Tarea', max_length=256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.clasificacion)


class Nom_Prioridad_Tarea(models.Model):
	prioridad = models.CharField('Tipo de Prioridad', max_length=256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.prioridad)


class Nom_Estado_Tarea(models.Model):
	estado = models.CharField('Tipo de Estado', max_length=256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.estado)

class Nom_Frecuencia_Tarea(models.Model):

	nombre = models.CharField('Tipo de Frecuencia', max_length=256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.estado)


class Tarea(models.Model):
	tarea = models.CharField('Nombre de la Tarea', max_length=256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length=256, blank=True, null=True)

	clasificacion = models.ForeignKey(Nom_Clasificacion_Tarea, max_length=256, blank=True, null=True, on_delete=models.CASCADE)
	prioridad = models.ForeignKey(Nom_Prioridad_Tarea, max_length=256, blank=True, null=True, on_delete=models.CASCADE)
	estado = models.ForeignKey(Nom_Estado_Tarea, max_length=256, blank=True, null=True, on_delete=models.CASCADE)
	categoria = models.ForeignKey(Nom_Categoria_Tarea, max_length=256, blank=True, null=True, on_delete=models.CASCADE)

	freg = models.DateField('Fecha de Registro', auto_now_add=True)
	fini = models.DateTimeField('Fecha de Inicio', default=datetime.datetime.today())
	ffin = models.DateTimeField('Fecha de Finalizacion',default=datetime.datetime.today())

	responsable = models.CharField('Responsable', max_length=256, blank=True, null=True)
	participantes = models.ManyToManyField(Trabajador, max_length=256)

	activo = models.BooleanField('Estado', max_length=256, blank=True)

	def __str__(self):
		return '%s' % (self.tarea)
