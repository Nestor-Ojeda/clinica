from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *



urlpatterns = [
#----------------CRUD Persona--------------------------------------------------------
	path('crear_persona/', CrearPersona.as_view(), name = 'crear_persona'),
	path('listar_persona', ListadoPersona.as_view(), name = 'listar_persona'),
	path('editar_persona/<int:pk>', ActualizarPersona.as_view(), name = 'editar_persona'),
	path('persona_confirm_delete/<int:pk>', EliminarPersona.as_view(), name='persona_confirm_delete'),

#---------------CRUD Obra Social------------------------------------------------------

	path('crear_obra_social', CrearObraSocial.as_view(), name='crear_obra_social'),
	path('listar_obra_social', ListadoObraSocial.as_view(), name='listar_obra_social'),
	path('editar_obra_social/<int:pk>', ActualizarObraSocial.as_view(), name='editar_obra_social'),
	path('obrasocial_confirm_delete/<int:pk>', EliminarObraSocial.as_view(), name='obrasocial_confirm_delete'),



]