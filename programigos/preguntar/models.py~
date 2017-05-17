# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Pregunta(models.Model):
	asunto = models.CharField(max_length=200)
	descripcion = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.asunto

	def publicadoHoy(self):
		return self.fecha.date() == timezone.now().date()
	publicadoHoy.boolean = True
	publicadoHoy.descripcionCorta = 'Preguntado hoy?'


class Respuesta(models.Model):
	Pregunta = models.ForeignKey(Pregunta)
	contenido = models.TextField()
	mejor = models.BooleanField("The Best is ",default=False)

	def __str__(self):
		return self.contenido
