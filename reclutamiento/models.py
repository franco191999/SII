import datetime
from django.db import models
from unidad.models import *

class comision(models.Model):
	comision = models.CharField('Comision', max_length=256)
	comentarioe = models.CharField('Comentario', max_length=256)
	
	def __str__(self):
		return '%s' % (self.estadoe)
class estomatologia(models.Model):
	estadoe = models.CharField('Estado Estomatologico', max_length=256)
	comentarioe = models.CharField('Comentario', max_length=256)
	
	def __str__(self):
		return '%s' % (self.estadoe)

class salud(models.Model):
	estados = models.CharField('Estado de Salud', max_length=256)
	comentarios = models.CharField('Comentario', max_length=256)
	
	def __str__(self):
		return '%s' % (self.estados)

class familia(models.Model):
	estadof = models.CharField('Estado de Familiar', max_length=256)
	comentariof = models.CharField('Comentario', max_length=256)
	
	def __str__(self):
		return '%s' % (self.estadof)
		
class llamado(models.Model):
	nombre = models.CharField('Nombre', max_length=256)
	fecha = models.DateField('Fecha')
	
	def __str__(self):
		return '%s' % (self.nombre)

class recluta(models.Model):
	nombre = models.CharField('Nombre', max_length=80, blank=True, null=True)
	ci = models.CharField('Carnet de Identidad', max_length=11, blank=True, null=True)
	direccion = models.CharField('Direccion', max_length=150, blank=True, null=True)
	c_estudios = models.CharField('Centro de Estudios', max_length=150, blank=True, null=True)
	c_trabajo = models.CharField('Centro de Trabajo', max_length=150, blank=True, null=True)
	municipio = models.ForeignKey(Nom_Municipio, max_length=250, blank=True, null=True, on_delete=models.CASCADE)
	area = models.CharField('Area de Salud', max_length=150, blank=True, null=True)
	centro = models.CharField('Centro Medico', max_length=150, blank=True, null=True)
	antecedentes = models.CharField('Antecedentes Patologicos Faniliares', max_length=500, blank=True, null=True)
	documentacion = models.BooleanField('Documentacion Pendiente', max_length = 256, blank=True, default=False)
	investigacion = models.BooleanField('Investigacion Pendiente', max_length = 256, blank=True, default=False)
	estomat = models.ForeignKey(estomatologia, blank=True, null=True, on_delete=models.CASCADE)
	saludd = models.ForeignKey(salud, blank=True, null=True, on_delete=models.CASCADE)
	familiaa = models.ForeignKey(familia, blank=True, null=True, on_delete=models.CASCADE)
	llamadoo = models.ForeignKey(llamado, blank=True, null=True, on_delete=models.CASCADE)
	registrado = models.DateTimeField('Registrado', auto_now_add=True)

	def __str__(self):
		return '%s' % (self.nombre)

class nom_categoria(models.Model):
	nombrec = models.CharField('Categoria', max_length=256)
	
	def __str__(self):
		return '%s' % (self.nombrec)

class nom_especialidad(models.Model):
	nombree = models.CharField('Especialidad', max_length=256)
	
	def __str__(self):
		return '%s' % (self.nombree)

class registro(models.Model):
	recluta = models.ForeignKey(recluta, on_delete=models.CASCADE)
	categoria = models.ForeignKey(nom_categoria, on_delete=models.CASCADE)
	especialidad = models.ForeignKey(nom_especialidad, on_delete=models.CASCADE)
	comentario = models.CharField('Comentario', max_length=256, blank=True, null=True)
	fecha = models.DateField('Fecha',auto_now_add=True)
	confirmacion = models.BooleanField('Confirmar Reclutamiento', max_length = 256, blank=True, default=False)
	comision = models.ForeignKey(comision, max_length=256, on_delete=models.CASCADE)
	registrado = models.DateTimeField('Registrado', auto_now_add=True)

	def __str__(self):
		return '%s' '%s' '%s' '%s' '%s' % (self.recluta.nombre, ' - ', self.comision, ' - ', self.fecha)
