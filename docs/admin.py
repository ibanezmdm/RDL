from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Servidor)
admin.site.register(models.Area)
admin.site.register(models.Dia)
admin.site.register(models.Solicitante)
admin.site.register(models.Reporte)
admin.site.register(models.TipoPaso)
admin.site.register(models.Paso)
admin.site.register(models.TipoFuente)
admin.site.register(models.RequisitoPaso)
