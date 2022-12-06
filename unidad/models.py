from django.db import models
directorio_fotografias = '%s/%s'


class Nom_Tipo_Unidad(models.Model):
	tipo = models.CharField('Tipo de Unidad', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.tipo)

class Nom_Perfil_Unidad(models.Model):
	perfil = models.CharField('Perfil de la Unidad', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.perfil)

class Nom_Provincia(models.Model):
	municipio = models.CharField('Provincia', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.municipio)

class Nom_Municipio(models.Model):
	provincia = models.ForeignKey(Nom_Provincia, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	codigo = models.CharField('Codigo', max_length = 256, blank=True, null=True)
	municipio = models.CharField('Municipio', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.municipio)

class Nom_Nivel_Unidad(models.Model):
     
	nivel = models.CharField('Nivel de Subordinacion de la Unidad', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.nivel)

class Unidad(models.Model):

	def get_upload_img_name(self, filename):
		upload_to = directorio_fotografias % ('imagen_unidad', filename)
		return upload_to

	codigo = models.CharField('Codigo unico de la Unidad', max_length = 256, blank=True, null=True)
	nombre = models.CharField('Nombre de la Unidad', max_length = 256, blank=True, null=True)
	direccion = models.CharField('Direccion', max_length = 256, blank=True, null=True)
	telefono = models.CharField('Telefono de la Recepcion', max_length = 256, blank=True, null=True)
	imagen = models.ImageField(upload_to=get_upload_img_name, blank=True, null=True)
	municipio = models.ForeignKey(Nom_Municipio, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	tipo = models.ForeignKey(Nom_Tipo_Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	perfil = models.ForeignKey(Nom_Perfil_Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	nivel = models.ForeignKey(Nom_Nivel_Unidad, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	subordinacion = models.ForeignKey('self', related_name='subordinados', max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.nombre)



class unidad_organizativa(models.Model):
	nombre = models.CharField('Nombre de la Unidad Organizativa', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.nombre)

class tipo_unidad_organizativa(models.Model):
	nombre = models.CharField('Tipo de Unidad Organizativa', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.nombre)



class Departamento(models.Model):
	tipouorganizativa = models.ForeignKey(tipo_unidad_organizativa, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	nombre = models.ForeignKey(unidad_organizativa, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	telefono = models.CharField('Telefono', max_length = 256, blank=True, null=True)
	unidad = models.ForeignKey(Unidad, related_name='departamento', max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)

	def __str__(self):
		return '%s' % (self.id)



class Nom_Tipo_Plaza(models.Model):
	tipoplaza = models.CharField('Tipo de Plaza', max_length = 256, blank=True, null=True)
	def __str__(self):
		return '%s' % (self.tipoplaza)

class Nom_Plaza(models.Model):
	plaza = models.ForeignKey(Nom_Tipo_Plaza, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	req_formales = models.TextField('Requisitos formales', max_length = 256, blank=True, null=True)
	salario = models.FloatField('Salario Basico', max_length = 256, blank=True, null=True)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s' % (self.plaza.tipoplaza)


class Plaza_Departamento(models.Model):
	plaza = models.ForeignKey(Nom_Plaza, max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	estado = models.CharField('Estado de la plaza', max_length = 256, blank=True, null=True)
	departamento = models.ForeignKey(Departamento, related_name='plaza_departamento',max_length = 256, blank=True, null=True, on_delete=models.CASCADE)
	activo = models.BooleanField('Estado', max_length = 256, blank=True)
	def __str__(self):
		return '%s del departamento %s de la unidad %s de %s' % (self.plaza.plaza.tipoplaza,self.departamento.nombre ,self.departamento.unidad,self.departamento.unidad.municipio)



