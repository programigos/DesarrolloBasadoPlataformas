# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from django.shortcuts import render
from django.http import HttpResponse,Http404
from preguntar.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response

# Create your views here.

def primer(request):
	pregunta = Pregunta.objects.all()
	return render_to_response("preguntar/primer.html",{"pregunta": pregunta})

def detalle(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta,pk=pregunta_id)
	return render_to_response("preguntar/detalle.html",{"pregunta": pregunta})

#[template_directory]/preguntar/primer.html