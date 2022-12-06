import datetime
from django.db import models
from unidad.models import *
from django.contrib.auth.models import User

perfil = (
	('Visualizador', 'Visualizador'),
	('Editor', 'Editor'),
	
	)

directorio_fotografias = '%s/%s'

class Nom_Cargo_Trabajador(models.Model):

	cargo = models.CharField('Funciones', max_length = 256, blank=True, null=True)
	resposabilidad = models.TextField('Responsabilidad', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.cargo)

class Nom_Titulo_Trabajador(models.Model):

	titulo = models.CharField('Categoria Profecional', max_length = 256, blank=True, null=True)
	especialidad = models.TextField('Especialidad', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.titulo)

class Nom_Habilidad_Trabajador(models.Model):

	habilidad = models.CharField('Habilidad', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length = 256, blank=True, null=True)
	
	def __str__(self):
		return '%s' % (self.habilidad)


class Trabajador(models.Model):


	def get_upload_img_name(self, filename):
		upload_to = directorio_fotografias % ('imagen_trabajador', filename)
		return upload_to

	nombre = models.CharField('Nombre', max_length = 256, blank=False, null=True)
	imagen = models.ImageField(upload_to=get_upload_img_name, blank=True, null=True)


	carne = models.CharField('Carne de Identidad', max_length = 256, blank=True, null=True)
	correo = models.EmailField('Correo electronico', max_length = 256, blank=False, null=True)

	direccion = models.CharField('Direccion', max_length = 256, blank=True, null=True)

	municipio = models.ForeignKey(Nom_Municipio, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)

	titulo = models.ForeignKey(Nom_Titulo_Trabajador, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	graduado = models.CharField('Graduado de ', max_length = 256, blank=True, null=True)

	telefono = models.CharField('Telefono', max_length = 256, blank=True, null=True)
	plaza_ocupa = models.OneToOneField(Plaza_Departamento, max_length = 256, blank=True, null=True, related_name='trabajador_plaza', on_delete=models.CASCADE)

	cargo = models.ManyToManyField(Nom_Cargo_Trabajador)

	registro = models.DateTimeField('Registrado',auto_now_add=True)
	estado = models.BooleanField('Estado', max_length = 256, blank=True)
	
	def __str__(self):
		return '%s' % (self.nombre)

class Perfil(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	trabajador = models.ForeignKey(Trabajador, max_length = 256, blank=True, related_name='perfil', on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.user.id)

class Userlog(models.Model):
	usuario =  models.CharField(max_length=250, blank=True)
	unidad =  models.CharField(max_length=250, blank=True)
	departamento =  models.CharField(max_length=250, blank=True)
	trabajador =  models.CharField(max_length=250, blank=True)
	accion = models.CharField(max_length=250, blank=True)
	numaccion = models.IntegerField(blank=True)
	ip= models.CharField( max_length=250,blank=True)
	fecha= models.DateTimeField('Registrado el: ',auto_now_add=True)
	def __str__(self):
		return 'log del usuario %s el %s' % (self.user, self.fecha)



class maquina(models.Model):
	pc = models.CharField('pc', max_length = 256, blank=True, null=True)
	ip = models.CharField('ip', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.pc)


class registromaquina(models.Model):
	pc = models.ForeignKey(maquina, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	fecha= models.DateTimeField('Registrado el: ',auto_now_add=True)
	estado = models.CharField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.pc)
