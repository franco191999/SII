from django.db import models
from unidad.models import *
directorio_fotografias = '%s/%s'

class tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.tipo)


class marca(models.Model):
	marca = models.CharField('Marca', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.marca)


class estadotecnico(models.Model):
	estadotecnico = models.CharField('Estado tecnico', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.estadotecnico)


class estadooperativo(models.Model):
	estadooperativo = models.CharField('Estado operativo', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.estadooperativo)


class combustible(models.Model):
	combustible = models.CharField('Combustible', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.combustible)


class neumatico(models.Model):
	neumatico = models.CharField('Neumatico', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.neumatico)


class bateria(models.Model):
	bateria = models.CharField('Bateria', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.bateria)

class demanda(models.Model):
	elementos = models.CharField('Elementos', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.elementos)

class funcion(models.Model):
	funcion = models.CharField('Funcion', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Activo',blank=True)
	def __str__(self):
		return '%s' % (self.funcion)

class parque(models.Model):


	def get_upload_img_name(self, filename):
		upload_to = directorio_fotografias % ('imagen_auto', filename)
		return upload_to

	unidad= models.ForeignKey(Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	matricula= models.CharField('Matricula', max_length = 256, blank=True, null=True)
	imagen = models.ImageField(upload_to=get_upload_img_name, blank=True, null=True)
	demanda= models.ManyToManyField(demanda, max_length = 256, blank=True)
	tipo= models.ForeignKey(tipo, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	marca = models.ForeignKey(marca, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	serie= models.CharField('Serie', max_length = 256, blank=True, null=True)
	motor= models.CharField('Motor', max_length = 256, blank=True, null=True)
	ficav= models.DateTimeField('FICAV',auto_now=False, auto_now_add=False, blank=True, null=True)
	circulacion= models.DateTimeField('Lic. de Circulacion',auto_now=False, auto_now_add=False, blank=True, null=True)
	operativa= models.DateTimeField('Lic. Operativa',auto_now=False, auto_now_add=False, blank=True, null=True)
	funcion= models.ForeignKey(funcion, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	estadotecnico= models.ForeignKey(estadotecnico, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	estadooperativo= models.ForeignKey(estadooperativo, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	combustible= models.ForeignKey(combustible, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	neumatico= models.ForeignKey(neumatico, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	bateria= models.ForeignKey(bateria, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	modelo= models.CharField('Modelo', max_length = 256, blank=True, null=True)
	comentario= models.TextField('Observaciones', max_length = 2048, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.matricula)
