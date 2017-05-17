# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse,Http404
from preguntar.models import Pregunta
from django.shortcuts import get_object_or_404
# Create your views here.

def primer(request):
	pregunta = Pregunta.objects.all()
	respuesta_string = "Preguntas <br/>"
	respuesta_string += '<br/>'.join(["id: %s,asunto: %s"%
	(p.id,p.asunto)for p in pregunta])
	return HttpResponse(respuesta_string)
'''
def detalle(request, pregunta_id):
	try:
		pregunta = Pregunta.objects.get(pk=pregunta_id)
	except Pregunta.DoesNotExist:
		raise Http404	
	return HttpResponse("%s ?" % pregunta.asunto)
'''
def detalle(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta,pk=pregunta_id)
	return HttpResponse("%s ?" % pregunta.asunto)

