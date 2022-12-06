from django.db import models
from unidad.models import *
directorio_fotografias = '%s/%s'

class articulo(models.Model):
	nombre = models.TextField('Nombre el Articulo', max_length=50, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.nombre)

class grupo(models.Model):
	numero = models.IntegerField('Numero',blank=True , null=False)
	nombre = models.TextField('Nombre', max_length=50, blank=True,null=True)

	def __str__(self):
		return '%s' % (self.numero)


class submayor(models.Model):
	submayor = models.IntegerField('Codigo', blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length=250, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.submayor)




class subgrupos(models.Model):
	codigo = models.IntegerField('Codigo',blank=True,null=True)
	numero = models.ForeignKey(grupo, max_length=5, blank=True, null=True, on_delete=models.CASCADE)
	descripcion = models.TextField('Descripcion',max_length=50,blank=True, null=True)
	def __str__(self):
		return '%s' % (self.descripcion)





class activos(models.Model):
	def get_upload_img_name(self, filename):
		upload_to = directorio_fotografias % ('imagen_qr_activo', filename)
		return upload_to

	imagen = models.ImageField(upload_to=get_upload_img_name, blank=True, null=True)
	subMayor = models.ForeignKey(submayor,max_length=50, blank=True, null=True, on_delete=models.CASCADE)
	inventario = models.IntegerField('Numero de Inventario', blank=True, null=True)
	cnmb = models.ForeignKey(subgrupos,max_length=50, blank=True, null=True, on_delete=models.CASCADE)
	nombre = models.ForeignKey(articulo, max_length=50, blank=True, null=True, on_delete=models.CASCADE)
	descripcion = models.TextField('Descripcion', max_length=250, blank=True, null=True)
	dpto = models.ForeignKey(Departamento, max_length=256, blank=True, on_delete=models.CASCADE)
	importe_activo = models.IntegerField('Importe',blank=True, null=True)

	def __str__(self):
		return '%s' % (self.inventario)

class orden_activos_fijos(models.Model):

	fecha = models.DateField()
	activos = models.ForeignKey(activos,max_length=50,blank=True, null=True, on_delete=models.CASCADE)
	fecha_alta = models.DateField('Fecha de Alta')
	doc_alta = models.IntegerField('Numero de Doc. de Alta',blank=True, null=True)
	importe = models.FloatField('Importe', max_length=50,blank=True, null=True)
	fecha_baja = models.DateField('Fecha de Baja')
	doc_baja = models.IntegerField('Numero de Doc. de Baja', blank=True, null=True)

	def __str__(self):
		return '%s' % (self.importe)







