from django.db import models

# Create your models here.
class Ciudad(models.Model):
	nombre = models.CharField(max_length=100)

	def as_json(self):
		return dict(nombre=self.nombre)

class Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	city = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING)

	def as_json(self):
		return dict(nombre=self.nombre, ciudad=self.city.nombre)

class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	passw = models.CharField(max_length=100)
	tiendas = models.ManyToManyField(Tienda)

	def as_json(self):
		return dict(nombre=self.nombre, email=self.email)

	def as_tiendas(self):
		return [tienda.nombre for tienda in self.tiendas.all()]