from django.contrib import admin

# Register your models here.
from .models import Ciudad, Tienda, Usuario

admin.site.register(Ciudad)
admin.site.register(Tienda)
admin.site.register(Usuario)