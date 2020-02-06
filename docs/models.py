from django.db import models
from django.conf import settings


class Servidor(models.Model):
	servidor = models.IntegerField(primary_key=True)
	ip = models.GenericIPAddressField(unique=True, verbose_name="ip del servidor")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Servidores"
		ordering = ['servidor']

	def __str__(self):
		return '%s'% (self.servidor)


class Area(models.Model):
	nombre = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = "Areas"
		ordering = ['nombre']

	def __str__(self):
		return '%s'% (self.nombre)


class Dia(models.Model):
	id = models.SmallIntegerField(primary_key=True)
	dia = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Dias"
		ordering = ['id']

	def __str__(self):
		return '%s'% (self.dia)



class Solicitante(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	area = models.ForeignKey(Area, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Solicitantes"
		ordering = ['apellido']

	def __str__(self):
		return '%s %s'% (self.nombre, self.apellido)


class Reporte(models.Model):
	URGENTE = 0
	IMPORTANTE = 1
	MEDIA = 2
	BAJA = 3
	PRIORIDAD=(
		(URGENTE, 'Urgente'),
		(IMPORTANTE, 'Importante'),
		(MEDIA, 'Media'),
		(BAJA, 'Baja'),
	)

	nombre = models.CharField(max_length=50)
	prioridad = models.IntegerField(
		choices=PRIORIDAD,
		default=MEDIA
	)
	solicitante = models.ForeignKey(Solicitante, on_delete=models.PROTECT)
	responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	dias = models.ManyToManyField(
		Dia,
		verbose_name="dias de actualizacion"
	)
	hora_actualizacion = models.TimeField(verbose_name="hora de actualizacion")
	repeticion = models.SmallIntegerField(verbose_name="tiempo de repeticion (hrs)", null=True, blank=True)
	servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Reportes"
		ordering = ['nombre']

	def __str__(self):
		return '%s (%s)'% (self.nombre, self.solicitante)


class TipoPaso(models.Model):
	tipo = models.CharField(max_length = 50, verbose_name = "tipo de paso")

	def __str__(self):
		return '%s'% (self.tipo)


class Paso(models.Model):
	n_paso = models.SmallIntegerField()
	id_reporte = models.ForeignKey(Reporte, on_delete = models.CASCADE)
	nombre = models.CharField(max_length=40, verbose_name = "nombre del paso")
	tipo = models.ForeignKey(TipoPaso, on_delete = models.PROTECT, verbose_name = "tipo de paso")
	servidor = models.ForeignKey(Servidor, on_delete = models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		unique_together = ['n_paso', 'id_reporte']
		verbose_name_plural = "Pasos"
		ordering = ['id_reporte', 'n_paso']

	def __str__(self):
		return '%s %s'% (self.n_paso, self.nombre)


class TipoFuente(models.Model):
	tipo = models.CharField(max_length = 30, verbose_name="tipo de fuente")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name_plural = "Tipos de fuentes"
		ordering = ['tipo']

	def __str__(self):
		return '%s'% (self.tipo)


class RequisitoPaso(models.Model):
	id_paso = models.ForeignKey(Paso, on_delete = models.CASCADE)
	tipo_fuente = models.ForeignKey(TipoFuente, on_delete = models.PROTECT)
	nombre_fuente = models.CharField(max_length = 50, verbose_name = "nombre tabla fuente")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		verbose_name_plural = "Requisitos de paso"
		ordering = ['id', 'id_paso']

	def __str__(self):
		return '%s %s'% (self.tipo_fuente, self.nombre_fuente)