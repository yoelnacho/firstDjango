from django.db import models

#creamos nuestro modelo.
class Datos(models.Model):
	nombres = models.CharField(max_length=150)
	apellido = models.CharField(max_length=150)
	numero = models.IntegerField()
	direccion = models.CharField(max_length=260)

	#cuando imprimimos la clase Datos devuelve sus contenidos
	def __unicode__(self):
		#para pasar solu una vairable:
		#return self.nombres
		#si queremos pasar mas de una variable, seria asi:
		return "%s %s" % (self.nombres, self.apellido)