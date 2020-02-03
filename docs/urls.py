from django.urls import path
from . import views


app_name = 'docs'
urlpatterns = [
	# ** ex: /docs/
	path('', views.IndexView.as_view(), name='index'),

	# ** ex: /docs/1/
	path('<int:pk>/', views.ReporteView.as_view(), name='reporte'),

	# ** ex: /docs/1/pasos
	path('<int:id_reporte>/pasos/', views.pasos_reporte, name='pasos'),
]