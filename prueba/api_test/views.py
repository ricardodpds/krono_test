import json
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Ciudad, Tienda, Usuario
from .serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

#Endpoint 1 | Usuarios dada una tienda
def get_users(request,shopid):
		queryset = Usuario.objects.filter(tiendas__id=shopid)
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

def get_tiendas_by_city(request,user,city):	
		queryset = Usuario.objects.filter(id=user)
		if queryset.count() > 0 :
		    user = queryset[0]
		    return JsonResponse(user.as_tiendas_citys(city), safe=False)
		else:
		    return JsonResponse( [] , safe=False)	

#Errores
def get_error_id(request):
	return JsonResponse( { 'Error': 'Id incorrecto | Intente: url/id/'}, status=401)

def get_error_shops_city(request):
	return JsonResponse( { 'Error': 'Ids incorrectos | Intente: url/user={id}&city={id}/'}, status=401)
