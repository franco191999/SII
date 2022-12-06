import datetime
from django.utils.timezone import now
from django.db import models
from unidad.models import *

directorio = '%s/%s'

class categorias(models.Model):

	categoria = models.CharField('Categorias', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.categoria)

class imagenes(models.Model):

	def get_upload_img_name(self, filename):
		upload_to = directorio % ('imagenes_galeria', filename)
		return upload_to

	unidad = models.CharField('Unidad', max_length = 256, blank=True, null=True)
	categoria = models.ForeignKey(categorias, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	titulo = models.CharField('Titulo', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length = 256, blank=True, null=True)
	imagen = models.ImageField(upload_to=get_upload_img_name, blank=True, null=True)
	registro = models.DateTimeField('Registrado', auto_now_add=True)
	estado = models.BooleanField('Estado', max_length = 256, blank=True)
	
	def __str__(self):
		return '%s - %s' % (self.titulo, self.imagen)
