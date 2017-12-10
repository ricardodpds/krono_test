from rest_framework import serializers
from .models import Ciudad
from .models import Tienda
from .models import Usuario

class CiudadSerializer(serializers.Serializer):
	class Meta:
		model = Ciudad
		fields = ('nombre')

class TiendaSerializer(serializers.Serializer):
	class Meta:
		model = Tienda
		fields = ('nombre', 'city')

class UsuarioSerializer(serializers.Serializer):
	class Meta:
		model = Usuario
		fields = ('id','nombre', 'email', 'tiendas')