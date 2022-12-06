from django.db import models

from transporte.models import *
from unidad.models import *
from rrhh.models import *
estados=(('Funcionando','Funcionando'),('Obsoleto','Obsoleto'),('Sin Funcionar','Sin Funcionar'))
class nom_marca(models.Model):
	marca = models.CharField('Marca', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.marca)

class unidad_radio(models.Model):
	unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
	def __str__(self):
		return '%s' % (self.unidad.nombre)

class movil (models.Model):
	chapa_movil = models.CharField('Chapa del Movil', max_length = 256, blank=True, null=True)
	marca_movil = models.CharField('Marca del Movil', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s con chapa %s' % (self.marca_movil,self.chapa_movil)


class estaciones_fijas(models.Model):
	marca = models.ForeignKey(nom_marca, on_delete=models.CASCADE)
	indicativo = models.CharField('Indicativo', max_length = 128, unique=True,)
	modelo = models.CharField('Modelo', max_length = 256, blank=True, null=True)
	estado = models.CharField('Estado de la estacion fija', max_length = 256, choices = estados, default = 'Funcionando')
	ubicacion=models.ForeignKey(Departamento, on_delete=models.CASCADE)
	def __str__(self):
		return 'Radio con marca %s de modelo %s' % (self.marca,self.modelo)

class estaciones_movil(models.Model):

	marca = models.ForeignKey(nom_marca, on_delete=models.CASCADE)
	indicativo = models.CharField('Indicativo', max_length = 128, unique=True,)
	modelo = models.CharField('Modelo', max_length = 256, blank=True, null=True)
	movil = models.OneToOneField(parque, unique=True, null=True, on_delete=models.CASCADE)
	estado = models.CharField('Estado de la estacion movil', max_length = 256, choices = estados, default = 'Funcionando')
	ubicacion=models.ForeignKey(Departamento, on_delete=models.CASCADE)
	def __str__(self):
		return '%s' % (self.indicativo)

class estaciones_portatiles(models.Model):

	marca = models.ForeignKey(nom_marca, on_delete=models.CASCADE)
	indicativo = models.CharField('Indicativo', max_length = 128, unique=True,)
	modelo = models.CharField('Modelo', max_length = 256, blank=True, null=True)
	estado = models.CharField('Estado de la estacion portatil', max_length = 256, choices = estados, default = 'Funcionando')
	responsable=models.ForeignKey(Trabajador, on_delete=models.CASCADE)
	def __str__(self):
		return '%s' % (self.indicativo)

class estaciones_repetidoras(models.Model):

	marca = models.ForeignKey(nom_marca, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 256, blank=True, null=True)
	ubicacion=models.CharField('Ubicacion de la estacion', max_length = 256, blank=True, null=True)
	estado = models.CharField('Estado de la estacion repetidora', max_length = 256, choices = estados, default = 'Funcionando')

	def __str__(self):
		return '%s' % (self.ubicacion)
