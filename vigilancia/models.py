import datetime
from django.db import models
from unidad.models import *
from rrhh.models import *


class universotratamientofocal(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	universo = models.CharField('Universo', max_length = 200, blank=True, null=True)
	plandiario = models.CharField('Plan Diario', max_length = 200, blank=True, null=True)
	def __str__(self):
		return '%s - %s' % (self.universo, self.plandiario)

class universotratamientoadulticida(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	universo = models.CharField('Universo', max_length = 200, blank=True, null=True)
	plandiario = models.CharField('Plan Diario', max_length = 200, blank=True, null=True)
	def __str__(self):
		return '%s - %s' % (self.universo, self.plandiario)


class tratamientofocal(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	universo= models.ForeignKey(universotratamientofocal, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	depoinspecciondos  = models.CharField('Locales Inspeccionados  ', max_length = 200, blank=True, null=True)
	depocerrados= models.CharField('Locales Cerrados', max_length = 200, blank=True, null=True)
	depositostotal= models.CharField('Depositos Totales', max_length = 200, blank=True, null=True)
	depositospositivos= models.CharField('Depositos Positivos', max_length = 200, blank=True, null=True)
	innaexistentes = models.CharField('Inaccesibles Existentes', max_length = 200, blank=True, null=True)
	innainspeccionados     = models.CharField('Inaccesibles Inspeccionados', max_length = 200, blank=True, null=True)
	localpoadultos = models.CharField('Local + Adultos', max_length = 200, blank=True, null=True)
	localpolarv= models.CharField('Local + Larvas o Pupas', max_length = 200, blank=True, null=True)
	localpototal = models.CharField('Local + Totales', max_length = 200, blank=True, null=True)
	localpoindcasa = models.CharField('Local + Indice por Casa', max_length = 200, blank=True, null=True)
	localpoindbetau= models.CharField('Local + Indice Betau', max_length = 200, blank=True, null=True)
	actualizacion  = models.DateTimeField('Hora de Actualizacion ', auto_now_add=True)

class tratamientoadulticida(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	universo= models.ForeignKey(universotratamientoadulticida, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	plandiario= models.CharField('Plan Diario', max_length = 200, blank=True, null=True)
	tratadas= models.CharField('Tratadas', max_length = 200, blank=True, null=True)
	cerrados= models.CharField('Cerradas', max_length = 200, blank=True, null=True)
	manzanasuniverso= models.CharField('Universo Manzanas', max_length = 200, blank=True, null=True)
	manzanastratadas= models.CharField('Manzanas Tratadas', max_length = 200, blank=True, null=True)
	localuniverso= models.CharField('Universo de Locales', max_length = 200, blank=True, null=True)
	localratados= models.CharField('Local Tratados', max_length = 200, blank=True, null=True)
	localcerradas= models.CharField('Local Cerradas', max_length = 200, blank=True, null=True)
	actualizacion  = models.DateTimeField('Hora de Actualizacion ', auto_now_add=True)

class recursos(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	rrhhhombres= models.CharField('Total de Hombres', max_length = 200, blank=True, null=True)
	rrhhhombrestrabajando= models.CharField('Hombres Trabajando', max_length = 200, blank=True, null=True)
	equipostotal = models.CharField('Total de Equipos ', max_length = 200, blank=True, null=True)
	equipostrabajando= models.CharField('Equipos Trabajando', max_length = 200, blank=True, null=True)
	equiposnosalieron= models.CharField('Equipos que No salieron', max_length = 200, blank=True, null=True)
	equiposrotos= models.CharField('Equipos Rotos', max_length = 200, blank=True, null=True)
	actualizacion  = models.DateTimeField('Hora de Actualizacion ',auto_now_add=True)


class centrospositivos(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	nombre= models.CharField('Nombre', max_length = 200, blank=True, null=True)
	organismo= models.CharField('Organismo', max_length = 200, blank=True, null=True)
	direccion= models.CharField('Direccion', max_length = 200, blank=True, null=True)
	depositos= models.CharField('Depositos', max_length = 200, blank=True, null=True)
	clasificacion= models.CharField('Clasificacion', max_length = 200, blank=True, null=True)
	actualizacion  = models.DateTimeField('Hora de Actualizacion ', auto_now_add=True)

class centroscerrados(models.Model):
	unidad= models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	nombre= models.CharField('Nombre', max_length = 200, blank=True, null=True)
	organismo= models.CharField('Organismo', max_length = 200, blank=True, null=True)
	direccion= models.CharField('Direccion', max_length = 200, blank=True, null=True)
	actualizacion  = models.DateTimeField('Hora de Actualizacion ', auto_now_add=True)

class albopictus(models.Model):
	unidad = models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	focos = models.CharField('Focos', max_length = 200, blank=True, null=True)
	tbajo = models.CharField('Tanques Bajos', max_length = 200, blank=True, null=True)
	telev = models.CharField('Tanques Elevados', max_length = 200, blank=True, null=True)
	ciste = models.CharField('Cisternas', max_length = 200, blank=True, null=True)
	a4odep = models.CharField('A4', max_length = 200, blank=True, null=True)
	artnodestruible = models.CharField('Artesanales No Destruibles', max_length = 200, blank=True, null=True)
	artdestruible = models.CharField('Artesanales Destruibles', max_length = 200, blank=True, null=True)
	naturales = models.CharField('Naturales', max_length = 200, blank=True, null=True)
	eresliq = models.CharField('Residuos L', max_length = 200, blank=True, null=True)
	depvigi = models.CharField('Depositos Vigilancia', max_length = 200, blank=True, null=True)
	adultos = models.CharField('Adultos', max_length = 200, blank=True, null=True)
	fecha  = models.DateField('Fecha')
	actualizacion  = models.DateTimeField('Hora de Actualizacion', auto_now_add=True)


class centrospriorizados(models.Model):
	unidad = models.ForeignKey(Unidad, max_length = 200, blank=True, null=True, on_delete=models.CASCADE)
	ciplan = models.CharField('Centros Inspeccionados Plan', max_length = 200, blank=True, null=True)
	cireal = models.CharField('Centros Inspeccionados Real', max_length = 200, blank=True, null=True)
	larvitrampasinstaladas = models.CharField('Larvitrampas Instaladas', max_length = 200, blank=True, null=True)
	larvitrampaspositivas = models.CharField('Larvitrampas Positivas', max_length = 200, blank=True, null=True)
	epaaeg = models.CharField('Especie Predominante Aedes Aegipti', max_length = 200, blank=True, null=True)
	epaalb = models.CharField('Especie Predominante Aedes Albupico', max_length = 200, blank=True, null=True)
	epatan = models.CharField('Especie Predominante Aedes Taen.', max_length = 200, blank=True, null=True)
	epaalbm = models.CharField('Especie Predominante Aedes Almbom', max_length = 200, blank=True, null=True)
	epoe = models.CharField('Otras Especies predominantes', max_length = 200, blank=True, null=True)
	otros = models.CharField('Otros Vectores', max_length = 200, blank=True, null=True)
	moscas = models.CharField('Moscas', max_length = 200, blank=True, null=True)
	cucarachas = models.CharField('Cucarachas', max_length = 200, blank=True, null=True)
	roedores = models.CharField('Roedores', max_length = 200, blank=True, null=True)
	larvasgeneral = models.CharField('Larvas general', max_length = 200, blank=True, null=True)
	adulreposo = models.CharField('Adultos en Reposo', max_length = 200, blank=True, null=True)
	encebohumano = models.CharField('En Cebo Humano', max_length = 200, blank=True, null=True)
	fecha  = models.DateField('Fecha')
	actualizacion  = models.DateTimeField('Hora de Actualizacion',auto_now_add=True)
