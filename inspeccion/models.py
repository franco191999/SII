from django.db import models
from rrhh.models import *
from unidad.models import *
from tareas.models import *

class Nom_Estado_Deficiencia(models.Model):
	estado = models.CharField('Tipo de Estado', max_length = 250, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 250, blank=True)
	def __str__(self):
		return '%s' % (self.estado)
		
class Nom_Aspecto_Deficiencia(models.Model):
	aspecto = models.CharField('Tipo de Estado', max_length = 250, unique=True, null=True)
	activo = models.BooleanField('Estado', max_length = 250, blank=True)
	def __str__(self):
		return '%s' % (self.aspecto)

class Nom_Tipo_Visita(models.Model):
	tipo = models.CharField('Tipo de Tarea', max_length = 250, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 250, blank=True)
	def __str__(self):
		return '%s' % (self.tipo)


class Visita(models.Model):
	tipo = models.ForeignKey(Nom_Tipo_Visita, max_length = 250, blank=True, null=True, on_delete=models.CASCADE)
	unidad = models.ForeignKey(Unidad, related_name='visitas',max_length = 250, blank=True, null=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField('Fecha de la visita',default=datetime.datetime.now())
	visitado = models.CharField('Visitado', max_length = 250, blank=True, null=True)
	participantes = models.ManyToManyField(Trabajador, max_length = 250, blank=True)
	activo = models.BooleanField('Estado', max_length = 250, blank=True)
	def __str__(self):
		return 'Visita a la unidad %s de %s el %s' % (self.unidad.nombre,self.unidad.municipio.municipio,self.fecha)

class Deficiencia(models.Model):
	visita = models.ForeignKey(Visita,related_name='deficiencias', max_length = 250, blank=True, null=True, on_delete=models.CASCADE)
	deficiencia = models.CharField('Deficiencia', max_length = 250, blank=True, null=True)
	estado = models.ForeignKey(Nom_Estado_Deficiencia, max_length = 250, blank=True, null=True, on_delete=models.CASCADE)
	aspecto = models.ForeignKey(Nom_Aspecto_Deficiencia, max_length = 250, blank=True, null=True, on_delete=models.CASCADE)
	observaciones = models.TextField('Observaciones', max_length = 250, blank=True, null=True)
	fechafin = models.DateTimeField('Fecha de cierre de la deficiencia', null=True)
	puntoaspecto = models.CharField('punto de aspecto', max_length = 250, blank=True, null=True)
	tarea = models.ManyToManyField(Tarea,through='deficienciasXtareas') 
	activo = models.BooleanField('Estado', max_length = 250, blank=True)
	def __str__(self):
		return 'Deficiencia %s detectada en la unidad %s de %s el %s' % (self.deficiencia,self.visita.unidad.nombre,self.visita.unidad.municipio.municipio,self.visita.fecha)

class deficienciasXtareas(models.Model): 
	tarea = models.ForeignKey(Tarea,related_name='deficient', on_delete=models.CASCADE) 
	deficiencia = models.ForeignKey(Deficiencia, on_delete=models.CASCADE) 
