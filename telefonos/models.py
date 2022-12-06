from django.db import models
from unidad.models import *

# Create your models here.


class Pizarra(models.Model):
	
	departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
	numero	= models.CharField('Numero', max_length = 8, blank=False, null=False)
	troncos	= models.IntegerField('Troncos', blank=False, null=False)
	marca	= models.CharField('Marca', max_length = 128, blank=True, null=True)
	modelo	= models.CharField('Modelo', max_length = 128, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.numero)	


class Telefono_Fijo(models.Model):
	
	departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
	numero	= models.CharField('Numero', max_length = 10, blank=False, null=False)

	def __str__(self):
		return '%s' % (self.numero)	
		
		
class Extencion(models.Model):
	
	departamento=models.ForeignKey(Departamento, on_delete=models.PROTECT)
	pizarra=models.ForeignKey(Pizarra, on_delete=models.PROTECT)
	numero	= models.CharField('Numero', max_length = 6, blank=False, null=False)
	
	def __str__(self):
		return '%s -- %s' % (self.pizarra, self.numero)		
	
	
