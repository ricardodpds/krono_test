import json
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Ciudad, Tienda, Usuario
from .serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

#Endpoint 1 | Usuarios dada una tienda
def get_users(request,shopid):
		queryset = Usuario.objects.filter(tiendas__id=shopid)
		return JsonResponse({ 'response':[ob.as_json() for ob in queryset], 'code': '0'}, safe=False)

#Endpoint 2 | Tiendas dado un id de usuario
def get_tiendas_by_id(request,userid):		
		queryset = Usuario.objects.filter(id=userid)
		if queryset.count() > 0:
		    user = queryset[0]
		    return JsonResponse({ 'response':user.as_tiendas(), 'code': '0'}, safe=False)
		else:
		    return JsonResponse( { 'response':[], 'code': '0'} , safe=False)	
#Endpoint 3 | Todas las tiendas de una ciudad, asociadas a un usuario

def get_tiendas_by_city(request,user,city):	
		queryset = Usuario.objects.filter(id=user)
		if queryset.count() > 0 :
		    user = queryset[0]
		    return JsonResponse({ 'response':user.as_tiendas_citys(city), 'code': '0'}, safe=False)
		else:
		    return JsonResponse( { 'response':[], 'code': '0'} , safe=False)	

#Errores
def get_error_id(request):
	return JsonResponse( { 'response': 'Error: Id incorrecto | Intente: url/id/', 'code': '1'}, status=401)

def get_error_shops_city(request):
	return JsonResponse( { 'response': 'Error: Ids incorrectos | Intente: url/user={id}&city={id}/', 'code': '1'}, status=401)
