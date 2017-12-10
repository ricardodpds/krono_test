import json
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Ciudad, Tienda, Usuario
from .serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

#Endpoint 1 | Usuarios dada una tienda
def get_users(request,nombre):
		nombre = nombre.replace("+"," ") # En el caso de que tengan espacios los nombres, ejemplo : 'Alfombras Shop' en la url => 'Alfombras+Shop'
		queryset = Usuario.objects.filter(tiendas__nombre=nombre)
		return JsonResponse([ob.as_json() for ob in queryset], safe=False)

#Endpoint 2 | Tiendas dado un id de usuario
def get_tiendas_by_id(request,userid):		
		queryset = Usuario.objects.filter(id=userid)
		if queryset.count() > 0:
		    user = queryset[0]
		    return JsonResponse(user.as_tiendas(), safe=False)
		else:
		    return JsonResponse( [] , safe=False)	
#Endpoint 3 | Todas las tiendas de una ciudad, asociadas a un usuario

def get_tiendas_by_id(request,userid):		
		queryset = Usuario.objects.filter(id=userid)
		if queryset.count() > 0:
		    user = queryset[0]
		    return JsonResponse(user.as_tiendas(), safe=False)
		else:
		    return JsonResponse( [] , safe=False)		

#Errores
def get_error_id(request):
	return JsonResponse( { 'Error': 'Id de usuario incorrecto | Intente: url/id/'}, status=401)

def get_error(request):
	return JsonResponse( { 'Error': 'Nombre de tienda incorrecto | Intente: url/{Nombre de la tienda (ejemplo Licoreros)}/'}, status=401)
