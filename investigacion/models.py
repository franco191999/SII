
from django.db import models
from rrhh.models import *
from unidad.models import *


#############################
#### LISTO FUNCIONANDO ####
#############################
class tipo_publicacion(models.Model):
	tipo = models.CharField('Funciones', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)
#############################
#############################
#############################

#############################
#### LISTO FUNCIONANDO ####
#############################
class publicaciones(models.Model):
	titulo = models.CharField('Titulo', max_length = 256, blank=True, null=True)
	tipo = models.ForeignKey(tipo_publicacion, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	nombrerevista = models.CharField('Nombre de la Revista', max_length = 256, blank=True, null=True)
	isbn = models.CharField('ISBN', max_length = 256, blank=True, null=True)
	nroautores = models.CharField('Cantidad de Autores', max_length = 256, blank=True, null=True)
	autorprincipal = models.ForeignKey(Trabajador, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	anno = models.DateField('Registrado')

	def __str__(self):
		return '%s' % (self.titulo)
#############################
#############################
#############################











#############################
#### LISTO FUNCIONANDO ####
#############################
class nom_lineamiento(models.Model):
	tipo = models.CharField('Lineamiento', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_estado(models.Model):
	tipo = models.CharField('Estado', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_clasificacion(models.Model):
	tipo = models.CharField('Clasificacion', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_tipo_salida(models.Model):
	tipo = models.CharField('Tipo salida', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_categ(models.Model):
	tipo = models.CharField('Categoria', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_tipo_proyecto(models.Model):
	tipo = models.CharField('Tipo de proyecto', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)

class nom_impacto(models.Model):
	tipo = models.CharField('Impacto', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipo)
#############################
#############################
#############################



#############################
#### LISTO FUNCIONANDO ####
#############################
class proyectos(models.Model):
	titulo= models.CharField('Titulo', max_length = 256, blank=True, null=True)
	lineamiento = models.ForeignKey(nom_lineamiento, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	estado = models.ForeignKey(nom_estado, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	clasificacion = models.ForeignKey(nom_clasificacion, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	linea_investig= models.CharField('Linea de Investigacion', max_length = 256, blank=True, null=True)
	tipo_salida = models.ForeignKey(nom_tipo_salida, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	categ = models.ForeignKey(nom_categ, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	tipo_proyecto = models.ForeignKey(nom_tipo_proyecto, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	fecha_inicio= models.DateField('Fecha de Inicio', max_length = 256, blank=True, null=True)
	impacto = models.ForeignKey(nom_impacto, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	fecha_entrada= models.DateField('Fecha de Entrada', max_length = 256, blank=True, null=True)
	fecha_terminacion= models.DateField('Fecha de Terminacion', max_length = 256, blank=True, null=True)
	causa_detenido= models.CharField('Causa de Terminacion', max_length = 256, blank=True, null=True)
	persona = models.ForeignKey(Trabajador, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	unidad = models.ForeignKey(Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)


	def __str__(self):
		return '%s' % (self.titulo)
#############################
#############################
#############################


