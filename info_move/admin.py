from django.contrib import admin
from .models import *
# Register your models here.
class user(admin.ModelAdmin):
	class Meta:
		model = Usuario
	list_display = ['rut','correo', 'nombre_usuario', 'nombre_completo']

class cond(admin.ModelAdmin):
	class Meta:
		model = Conductor
	list_display = ['identificador', 'nombre', 'puntaje' ]
class val(admin.ModelAdmin):
	class Meta:
		model = Valoracion
	list_display = ['identificador', 'emisor','receptor', 'puntaje' ]
class micro(admin.ModelAdmin):
	class Meta:
		model = Micro
	list_display = ['patente', 'recorrido' ]
admin.site.register(Usuario,user)
admin.site.register(Itinerario)
admin.site.register(Empresa)
admin.site.register(Paradero)
admin.site.register(Recorrido)
admin.site.register(Valoracion,val)
admin.site.register(Conductor,cond)
admin.site.register(Micro,micro)
admin.site.register(PasaPor)
admin.site.register(Realiza)
admin.site.register(Conduce)