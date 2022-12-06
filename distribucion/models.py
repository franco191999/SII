#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from django.db import models
from unidad.models import *


class tipomovimiento(models.Model):
	nombre=models.CharField('Tipo',max_length=30,blank=True,null=True)
	def __str__(self):
		return '%s' % (self.nombre)

class mesa(models.Model):
	nombre=models.CharField('No Mesa',max_length=30,blank=True,null=True)
	def __str__(self):
		return '%s' % (self.nombre)

class pedido(models.Model):
	comentario=models.CharField('Comentario',max_length=20148,blank=True,null=True)
	pedido=models.DateTimeField('Momento',max_length=30,blank=True,null=True)
	def __str__(self):
		return '%s' % (self.pedido)


class movimiento(models.Model):

	pedido=models.ForeignKey(pedido,max_length=30,blank=True,null=True, on_delete=models.CASCADE)
	mesa=models.ForeignKey(mesa,max_length=30,blank=True,null=True, on_delete=models.CASCADE)
	tipomovimiento=models.ForeignKey(tipomovimiento,max_length=30,blank=True,null=True, on_delete=models.CASCADE)
	unidad=models.ForeignKey(Unidad,max_length=30,blank=True,null=True, on_delete=models.CASCADE)
	cantidad=models.CharField('Cantidad',max_length=30,blank=True,null=True)
	importe=models.FloatField('Importe',max_length=30,blank=True,null=True)
	pcosto=models.CharField('Precio de Costo',max_length=2048,blank=True,null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now_add=True)

	def __str__(self):
		return '%s' % (self.id)




