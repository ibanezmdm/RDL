from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Reporte


class IndexView(generic.ListView):
	template_name = 'docs/index.html'
	context_object_name = 'reporte_list'

	def get_queryset(self):
		return Reporte.objects.order_by('id')



class ReporteView(generic.DetailView):
	model = Reporte
	template_name = 'docs/reporte.html'



def pasos_reporte(request, id_reporte):
  detalle = "Estas buscando los pasos del reporte %s."
  return HttpResponse(detalle % id_reporte)