from django.db import models
from rrhh.models import *


class nom_tipo_pc(models.Model):
	tipo_pc = models.CharField('Tipo de PC', max_length = 50, blank=True, null=True)
	def __str__(self):
		return self.tipo_pc

class so(models.Model):
	so = models.CharField('Sistema Operativo', max_length = 50, blank=True, null=True)
	def __str__(self):
		return self.so

class estado(models.Model):
	status = models.CharField(max_length = 50, blank=True, null=True)
	def __str__(self):
		return self.status


class pc(models.Model):
	nombre = models.CharField('Nombre de la Maquina', max_length = 50, blank=True, null=True)
	responsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	so = models.ForeignKey(so, verbose_name='Sistema Operativo', on_delete=models.CASCADE)
	tipo_pc = models.ForeignKey(nom_tipo_pc, verbose_name='Tipo de Estacion', on_delete=models.CASCADE)
	id_estado = models.ForeignKey(estado, verbose_name="Estado", blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.tipo_pc




#DEFINIENDO DATOS DE LA MOTHERBOARD
class nom_board_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_socket(models.Model):
	socket = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.socket


class board_pc(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	board_socket = models.ForeignKey(nom_socket, verbose_name='Socket de la Board', on_delete=models.CASCADE)
	board_marca = models.ForeignKey(nom_board_marca, verbose_name='Marca de la Board', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	def __str__(self):
		return self.board_socket
#########################################





#DEFINIENDO DATOS DE LA PROCESADOR
class nom_procesador_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_procesador_velocidad(models.Model):
	velocidad = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.velocidad

class procesador(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	procesador_socket = models.ForeignKey(nom_socket, verbose_name='Socket del Micro', on_delete=models.CASCADE)
	procesador_marca = models.ForeignKey(nom_procesador_marca, verbose_name='Marca del Micro', on_delete=models.CASCADE)
	procesador_velocidad = models.ForeignKey(nom_procesador_velocidad, verbose_name='Velocidad', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.procesador_marca
#########################################





#DEFINIENDO DATOS DE LA RAM
class nom_ram_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_ram_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo
		
class nom_ram_velocidad(models.Model):
	velocidad = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.velocidad

class ram(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	ram_tipo = models.ForeignKey(nom_ram_tipo, verbose_name='Tipo de RAM', on_delete=models.CASCADE)
	ram_marca = models.ForeignKey(nom_ram_marca, verbose_name='Marca de la RAM', on_delete=models.CASCADE)
	ram_velocidad = models.ForeignKey(nom_ram_velocidad, verbose_name='Velocidad', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.ram_tipo
#########################################





#DEFINIENDO DATOS DE LA HDD
class nom_hdd_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_hdd_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo
		
class nom_hdd_capacidad(models.Model):
	capacidad = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.capacidad

class hdd(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	hdd_tipo = models.ForeignKey(nom_hdd_tipo, verbose_name='Tipo de Disco Duro', on_delete=models.CASCADE)
	hdd_marca = models.ForeignKey(nom_hdd_marca, verbose_name='Marca', on_delete=models.CASCADE)
	hdd_capacidad = models.ForeignKey(nom_hdd_capacidad, verbose_name='Capacidad en GB', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.hdd_marca
#########################################





#DEFINIENDO DATOS DE LECTOR/QUEMADOR DE CD/DVD
class nom_cddvd_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_cddvd_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class nom_cddvd_utilidad(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class cddvd(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	cddvd_tipo = models.ForeignKey(nom_cddvd_tipo, verbose_name='Tipo de Dispositivo', on_delete=models.CASCADE)
	cddvd_marca = models.ForeignKey(nom_cddvd_marca, verbose_name='Marca', on_delete=models.CASCADE)
	cddvd_utilidad = models.ForeignKey(nom_cddvd_utilidad, verbose_name='Utilidad', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.cddvd_marca
#########################################





#DEFINIENDO DATOS DE LA FUENTE
class nom_fuente_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_fuente_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class fuente(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	fuente_tipo = models.ForeignKey(nom_fuente_tipo, verbose_name='Tipo de fuente', on_delete=models.CASCADE)
	fuente_marca = models.ForeignKey(nom_fuente_marca, verbose_name='Marca', on_delete=models.CASCADE)
	potencia = models.CharField('Potencia', max_length = 50, blank=True, null=True)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.fuente_marca
#########################################





#DEFINIENDO DATOS DE LA TARJETA DE VIDEO
class nom_tvideo_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_tvideo_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class tvideo(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	ftvideo_tipo = models.ForeignKey(nom_tvideo_tipo, verbose_name='Tipo de tarjeta de video', on_delete=models.CASCADE)
	tvideo_marca = models.ForeignKey(nom_tvideo_marca, verbose_name='Marca de la tarjeta', on_delete=models.CASCADE)
	capacidad = models.CharField('Capacidad', max_length = 50, blank=True, null=True)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.tvideo_marca
#########################################





#DEFINIENDO DATOS DE LA TARJETA DE SONIDO
class nom_tsonido_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_tsonido_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class tsonido(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	tsonido_tipo = models.ForeignKey(nom_tsonido_tipo, verbose_name='Tipo de tarjeta de Sonido', on_delete=models.CASCADE)
	tsonido_marca = models.ForeignKey(nom_tsonido_marca, verbose_name='Marca', on_delete=models.CASCADE)
	capacidad = models.CharField('Capacidad', max_length = 50, blank=True, null=True)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.tsonido_marca
#########################################





#DEFINIENDO DATOS DE LA TARJETA DE RED
class nom_tred_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_tred_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class nom_tred_velocidad(models.Model):
	velocidad = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class tred(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	tred_tipo = models.ForeignKey(nom_tred_tipo, on_delete=models.CASCADE)
	tred_marca = models.ForeignKey(nom_tred_marca, on_delete=models.CASCADE)
	tred_velocidad = models.ForeignKey(nom_tred_velocidad, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)

	def __str__(self):
		return self.tred_marca
#########################################





#DEFINIENDO DATOS DEL CHASIS
class nom_chasis_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_chasis_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class chasis(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	chasis_tipo = models.ForeignKey(nom_chasis_tipo, verbose_name='Tipo de Chasis', on_delete=models.CASCADE)
	chasis_marca = models.ForeignKey(nom_chasis_marca, verbose_name='Marca del Chasis', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.chasis_marca
#########################################





#DEFINIENDO DATOS DEL MODEM
class nom_modem_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_modem_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class modem(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	modem_tipo = models.ForeignKey(nom_modem_tipo, on_delete=models.CASCADE)
	modem_marca = models.ForeignKey(nom_modem_marca, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.modem_marca
#########################################





#DEFINIENDO DATOS DEL TECLADO
class nom_teclado_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_teclado_raton_tipo(models.Model):
	tipo = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class teclado(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	teclado_tipo = models.ForeignKey(nom_teclado_raton_tipo, verbose_name='Tipo de Teclado', on_delete=models.CASCADE)
	teclado_marca = models.ForeignKey(nom_teclado_marca, verbose_name='Marca del Teclado', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.teclado_marca
#########################################




#DEFINIENDO DATOS DEL TECLADO
class nom_raton_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class raton(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	raton_tipo = models.ForeignKey(nom_teclado_raton_tipo, verbose_name='Tipo de Raton', on_delete=models.CASCADE)
	raton_marca = models.ForeignKey(nom_raton_marca, verbose_name='Marca', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.teclado_marca
#########################################




#DEFINIENDO DATOS DE LAS BOCINAS
class nom_bocinas_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class raton(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	bocinas_marca = models.ForeignKey(nom_bocinas_marca, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.bocinas_marca
#########################################




#DEFINIENDO DATOS DEL MONITOR
class nom_monitor_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_monitor_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class nom_monitor_dimension(models.Model):
	dimension = models.CharField('Dimension', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.dimension

class monitor(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	monitor_marca = models.ForeignKey(nom_monitor_marca, verbose_name='Marca del Monitor', on_delete=models.CASCADE)
	monitor_dimension = models.ForeignKey(nom_monitor_dimension, verbose_name='Dimensiones', on_delete=models.CASCADE)
	monitor_tipo = models.ForeignKey(nom_monitor_tipo, verbose_name='Tipo', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.monitor_marca
#########################################





#DEFINIENDO DATOS DE LA IMPRESORA
class nom_impresora_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_impresora_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class nom_impresora_interface(models.Model):
	interface = models.CharField('Interface', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.interface

class impresora(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	impresora_marca = models.ForeignKey(nom_impresora_marca, verbose_name='Marca de la Impresora', on_delete=models.CASCADE)
	impresora_inteface = models.ForeignKey(nom_impresora_interface, verbose_name='Enlace con la PC', on_delete=models.CASCADE)
	impresora_tipo = models.ForeignKey(nom_impresora_tipo, verbose_name='Tipo', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.impresora_marca
#########################################








#DEFINIENDO DATOS DEL SCANNER
class nom_scanner_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_scanner_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class nom_scanner_dimension(models.Model):
	dimension = models.CharField('Dimension', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.dimension

class nom_scanner_interface(models.Model):
	interface = models.CharField('Interface', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.dimension

class scanner(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	scanner_marca = models.ForeignKey(nom_scanner_marca, on_delete=models.CASCADE)
	scanner_dimension = models.ForeignKey(nom_scanner_dimension, on_delete=models.CASCADE)
	scanner_interface = models.ForeignKey(nom_scanner_interface, on_delete=models.CASCADE)
	scanner_tipo = models.ForeignKey(nom_scanner_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.scanner_marca
#########################################





#DEFINIENDO DATOS DE LA UPS
class nom_ups_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_ups_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class ups(models.Model):
	pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	ups_marca = models.ForeignKey(nom_ups_marca, on_delete=models.CASCADE)
	ups_tipo = models.ForeignKey(nom_ups_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.ups_marca
#########################################










#DEFINIENDO DATOS DEL SWITCH
class nom_switch_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_switch_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class switch(models.Model):
	reponsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	switch_marca = models.ForeignKey(nom_switch_marca, on_delete=models.CASCADE)
	switch_tipo = models.ForeignKey(nom_switch_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)
	num_puertos = models.CharField(max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.switch_marca
#########################################










#DEFINIENDO DATOS DE LA CAMARA
class nom_camara_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_camara_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class camara(models.Model):
	reponsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	camara_marca = models.ForeignKey(nom_camara_marca, on_delete=models.CASCADE)
	camara_tipo = models.ForeignKey(nom_camara_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.switch_marca
#########################################











#DEFINIENDO DATOS DE LOS STICK 
class nom_stick_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_stick_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class stick(models.Model):
	reponsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	stick_marca = models.ForeignKey(nom_stick_marca, on_delete=models.CASCADE)
	stick_tipo = models.ForeignKey(nom_stick_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.switch_marca
#########################################






#DEFINIENDO DATOS DE LOS STICK 
class nom_stick_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_stick_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class stick(models.Model):
	reponsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	stick_marca = models.ForeignKey(nom_stick_marca, on_delete=models.CASCADE)
	stick_tipo = models.ForeignKey(nom_stick_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.switch_marca
#########################################





#DEFINIENDO DATOS DE LOS AP 
class nom_ap_marca(models.Model):
	marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.marca

class nom_ap_tipo(models.Model):
	tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	def __str__(self):
		return self.tipo

class ap(models.Model):
	reponsable = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	ap_marca = models.ForeignKey(nom_ap_marca, on_delete=models.CASCADE)
	ap_tipo = models.ForeignKey(nom_ap_tipo, on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	serie = models.CharField(max_length = 50, blank=True, null=True)
	activo = models.BooleanField('Activado', max_length = 50, blank=True)
	inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)

	def __str__(self):
		return self.switch_marca
#########################################






























#~ 
#~ 
#~ class telefonoip(models.Model):
	#~ representante = models.ForeignKey(Trabajador, max_length = 50, blank=True, null=True, on_delete=models.CASCADE)
	#~ tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	#~ marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	#~ modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	#~ velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)
	#~ serie = models.CharField('Numero de Serie', max_length = 50, blank=True, null=True)
	#~ inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ id_estado = models.ForeignKey(estado, verbose_name="Estado", on_delete=models.CASCADE)
	#~ def __str__(self):
		#~ return self.marca

#~ 
#~ 
#~ #DEFINIENDO DATOS DE LA LAPTOP
#~ class nom_laptop_marca(models.Model):
	#~ marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ def __str__(self):
		#~ return self.marca
#~ 
#~ class nom_laptop_tipo(models.Model):
	#~ tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ def __str__(self):
		#~ return self.tipo
#~ 
#~ class nom_laptop_tipo(models.Model):
	#~ tipo = models.CharField('Tipo', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ def __str__(self):
		#~ return self.tipo
#~ 
#~ class laptop(models.Model):
	#~ id_pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	#~ ap_marca = models.ForeignKey(nom_ap_marca, on_delete=models.CASCADE)
	#~ ap_tipo = models.ForeignKey(nom_ap_tipo, on_delete=models.CASCADE)
	#~ modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	#~ serie = models.CharField(max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	#~ velocidad = models.CharField('Velocidad', max_length = 50, blank=True, null=True)
#~ 
	#~ def __str__(self):
		#~ return self.switch_marca
#~ #########################################
#~ 
#~ class laptop(models.Model):
	#~ id_pc = models.ForeignKey(pc, blank=True, null=True, on_delete=models.CASCADE)
	#~ capacidad = models.CharField('Capacidad', max_length = 50, blank=True, null=True)
	#~ serie = models.CharField('Numero de Serie', max_length = 50, blank=True, null=True)
	#~ inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ id_estado = models.ForeignKey(estado, verbose_name="Estado", on_delete=models.CASCADE)




#~ 
#~ 
#~ 
#~ class datashow(models.Model):
	#~ marca = models.CharField('Marca', max_length = 50, blank=True, null=True)
	#~ modelo = models.CharField('Modelo', max_length = 50, blank=True, null=True)
	#~ serie = models.CharField('Numero de Serie', max_length = 50, blank=True, null=True)
	#~ inventario = models.CharField('Numero de Inventario', max_length = 50, blank=True, null=True)
	#~ activo = models.BooleanField('Activado', max_length = 50, blank=True)
	#~ id_estado = models.ForeignKey(estado, verbose_name="Estado", on_delete=models.CASCADE)
