from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import pytz

# Create your views here.
def home(request):
	return render(request, 'home.html')
def crear_valoracion(request):
	if request.method == 'POST':
		if(request.POST.get("cancelar") is not None):
			return redirect('cancelar_crear_comentario')
		form = ValoracionForm(request.POST)
		if request.POST.get("confirmar"):
			if form.is_valid():
				valoracion = Valoracion()
				valoracion.puntaje = form.cleaned_data['puntaje']
				valoracion.comentario= form.cleaned_data['comentario']
				usuario = request.user
				#usuario = Usuario.objects.get(id=usuario.identificador)
				valoracion.emisor = usuario
				conductor = Conductor.objects.get(id=request.POST.get("conductor_id"))
				timezone = pytz.timezone('Chile/Continental')
				actual = datetime.strptime(datetime.now(tz=timezone).strftime("%d/%m/%Y %H:%M:%S") , "%d/%m/%Y %H:%M:%S")
				valoracion.receptor = conductor
				valoracion.fecha = actual
				valoracion.save()
			else:
				mensaje = "Ha ocurrido un error, intenta publicar tu valoración nuevamente"
				form = ValoracionForm()
				return render(request,'alguna_template_de_error',{'form':form, 'error': mensaje})
			return render(request,'template_de_exito')
	else:
		form = ValoracionForm()
		return render(request, 'template_de_crear_comentario', {'form': form} )

@login_required()
def ver_perfil_usuario(request,pk):
	info_perfil = []
	try:
		us = Usuario.objects.get(id = pk)
		info_perfil.append(us.nombre_usuario)
		info_perfil.append(us.nombre_completo)
		info_perfil.append(us.correo)
		val = Valoracion.objects.filter(emisor=pk)
		info_perfil.append(val.size())
		#si val.size() no funciona
		#valoraciones = 0	
		#for v in val:		
		#valoraciones += 1
		#info_perfil.append(valoraciones)
	except:
		return render(request, 'perfil_error.html')
	return render(request, 'perfil_usuario.html', {'perfil': info_perfil})

@login_required()
def ver_perfil_conductor(request,pk):
	info_conductor = []
	try:
		conductor = Conductor.objects.get(id = pk)
		info_conductor.append(conductor.nombre)
		info_conductor.append(conductor.foto)
		info_conductor.append(conductor.puntaje)
		#info_conductor.append(filtrar_micro_por_chofer)
		val = Valoracion.objects.filter(receptor=pk).order_by('fecha')
	except:
		return render(request, 'perfil_error.html')
	return render(request, 'perfil_conductor.html', {'perfil': info_perfil, 'valoraciones': val})

def filtrar_micro_por_chofer(pk,hora_,fecha_):
	conductor = Conductor.objects.get(id = pk)
	posibles_micros = Conduce.objects.filter(fecha=fecha_).filter(conductor=pk)
	for p in posibles_micros:
		if(p.itinerario.inicio >= hora_ && p.itinerario.fin < hora_):
			return p.itinerario.micro

