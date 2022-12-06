from django.db import models
from tareas.models import *
from equipamiento.models import *
from rrhh.models import *
from unidad.models import *

directorio_documentos = '%s/%s'
directorio_ficheros = '%s/%s'

class Categoria(models.Model):
	
	categoria = models.CharField('estado', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.categoria)
		
class Ficheros(models.Model):

	nombre = models.TextField('nombre', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('descripcion', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('activo')
	unidad = models.ManyToManyField(Unidad)
	
	def __str__(self):
		return '%s' % (self.nombre)

class Objetivo(models.Model):
	
	objetivo = models.TextField('objetivo', max_length = 256, blank=True, null=True)
	
	
	def __str__(self):
		return '%s' % (self.objetivo)
		
class Tipo_web(models.Model):
	
	tipo = models.CharField('tipo', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.tipo)
		
class Ancho_banda(models.Model):
	
	ancho = models.CharField('ancho', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.ancho)

class Anno_unidad(models.Model):
	
	anno = models.DateTimeField('Anno',auto_now_add=True)
	unidad = models.ForeignKey(Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	objetivos = models.ManyToManyField(Objetivo, max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.unidad)
		
class Resultados(models.Model):
	
	resultado = models.TextField('resultado', max_length = 256, blank=True, null=True)
	categoria = models.ForeignKey(Categoria, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	observaciones = models.TextField('observaciones', max_length = 256, blank=True, null=True)
	tipo = models.BooleanField('Tipo')
	anno_unidad = models.ForeignKey(Anno_unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	

	def __str__(self):
		return '%s' % (self.resultado)
		
		
class Conectividad(models.Model):
	
	cant_cuentas = models.IntegerField(blank=True, null=True)
	unidad = models.ForeignKey(Unidad, related_name='conectividades', max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return '%s' % (self.cant_cuentas)


		
class P_web(models.Model):
	
	direccion = models.CharField('URL', max_length = 200, blank=True, null=True)
	tipo = models.ForeignKey(Tipo_web, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	observaciones = models.TextField('observaciones', max_length = 256, blank=True, null=True)
	conectividad = models.ForeignKey(Conectividad, related_name="p_web", max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	

	def __str__(self):
		return '%s' % (self.direccion)
		
class Enlaces(models.Model):
	
	tipo = models.CharField('Tipo de enlace', max_length = 256, blank=True, null=True)
	ancho_banda = models.ForeignKey(Ancho_banda, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	acceso = models.BooleanField('Internet')
	serv_ptes_ext = models.BooleanField('Paquetes')
	ip = models.GenericIPAddressField()
	conectividad = models.ForeignKey(Conectividad, related_name='enlacesXconectividad',max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	

	def __str__(self):
		return '%s' % (self.tipo)

class Aplicaciones(models.Model):

	def get_upload_file_name(self, filename):
		upload_to = directorio_documentos % ('documentos_aplicaciones', filename)
		return upload_to
	
	nombre = models.TextField('Nombre', max_length = 256, blank=True, null=True)
	comentario = models.TextField('Comentario', max_length = 256, blank=True, null=True)
	documento = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	estado = models.BooleanField('Estado')
	unidad = models.ManyToManyField(Unidad, max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.nombre)
		
class Documentos(models.Model):
	def get_upload_file_name(self, filename):
		upload_to = directorio_ficheros % ('documentos_ficheros', filename)
		return upload_to
	
	ficheros = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	unidad = models.ForeignKey(Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	documento = models.ForeignKey(Ficheros, blank=True, null=True, on_delete=models.CASCADE)


	def __str__(self):
		return '%s' % (self.documento.nombre)


