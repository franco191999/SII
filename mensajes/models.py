import datetime
from django.db import models
from rrhh.models import *
from django.contrib.auth.models import User

class categoria(models.Model):

	categoria = models.CharField('Categoria', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length = 256, blank=True, null=True)
	estado = models.BooleanField('Activo', max_length = 256)
	
	def __str__(self):
		return '%s' % (self.categoria)


class mensaje(models.Model):
	categoria = models.ForeignKey(categoria, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	asunto = models.CharField('Asunto ', max_length = 256, blank=True, null=True)
	texto = models.TextField('Texto', max_length = 256, blank=True, null=True)
	respuesta = models.TextField('Respuesta', max_length = 256, blank=True, null=True)
	estado = models.CharField('estado', max_length = 256, blank=True, null=True)

	activo = models.BooleanField('Activo')
	registro = models.DateTimeField('Registrado', auto_now_add=True)
	ip = models.CharField('Direccion IP', max_length = 256, blank=True, null=True)
	remitente = models.ForeignKey(User, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	destinatario = models.ManyToManyField(Trabajador, null=True,blank=True)

	def __str__(self):
		return '%s' % (self.asunto)
		
class eliminar_destinatario(models.Model):
	mensaje = models.ForeignKey(mensaje, on_delete=models.CASCADE)
	trabajador = models.ForeignKey(Trabajador, max_length = 256, blank=True, on_delete=models.CASCADE)
	eliminado = models.CharField('estado', max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.trabajador)

class mensaje_leido(models.Model):
	mensaje = models.ForeignKey(mensaje, on_delete=models.CASCADE)
	trabajador = models.ForeignKey(Trabajador, max_length = 256, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.trabajador)
