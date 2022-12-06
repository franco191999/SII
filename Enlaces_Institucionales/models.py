
from django.db import models
from unidad.models import *

class Enlaces_Institucionales(models.Model):
	
	institucion = models.CharField('institucion ', max_length = 256, blank=True, null=False)
	municipio = models.ForeignKey(Nom_Municipio, max_length = 256, blank=True, null=False, on_delete=models.CASCADE)
	numero_servicio = models.TextField('numero_servicio', max_length = 200, blank=True, null=False)
	ip_lan = models.CharField('ip_lan', max_length = 256, blank=True, null=False)
	ip_wan = models.CharField('ip_wan', max_length = 256, blank=True, null=False)
	velocidad = models.CharField('velocidad', max_length = 256, blank=True, null=False)
	observaciones = models.TextField('observaciones', max_length = 256, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.institucion)
		