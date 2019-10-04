from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import pytz
from info_move.forms import *
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	return render(request, 'index.html')


def ListaMicros(request):
	return render(request, 'Lista.html')

def ComentariosChofer(request):
	return render(request, 'CometariosChofer.html')

def CrearValoracion(request):
	if request.method == 'POST':
		if(request.POST.get("cancelar") is not None):
			return redirect('cancelar_crear_comentario')
		form = ValoracionForm(request.POST)
		if form.is_valid():
			valoracion = Valoracion()
			valoracion.puntaje = form.cleaned_data['puntaje']
			valoracion.comentario= form.cleaned_data['comentario']
			patente= form.cleaned_data['patente']
			valoracion.emisor = request.user
			timezone = pytz.timezone('Chile/Continental')
			actual = datetime.strptime(datetime.now(tz=timezone).strftime("%d/%m/%Y %H:%M:%S") , "%d/%m/%Y %H:%M:%S")
			conductor = patente_to_conductor(patente,datetime.strptime(datetime.now(tz=timezone).strftime("%d/%m/%Y") , "%d/%m/%Y"),actual.hour)
			if(conductor == None):
				mensaje = "Ha ocurrido un error, intenta publicar tu valoración nuevamente"
				form = ValoracionForm()
				return render(request,'alguna_template_de_error',{'form':form, 'error': mensaje})
			valoracion.receptor = conductor
			valoracion.fecha = datetime.strptime(datetime.now(tz=timezone).strftime("%d/%m/%Y") , "%d/%m/%Y")
			valoracion.save()
			return render(request,'template_de_exito')
		else:
			mensaje = "Ha ocurrido un error, intenta publicar tu valoración nuevamente"
			form = ValoracionForm()
			return render(request,'alguna_template_de_error',{'form':form, 'error': mensaje})
	else:
		form = ValoracionForm()
		return render(request, 'emitir_valoracion.html', {'form': form} )
def patente_to_conductor(patente,fecha,hora):
	itinerario = Itinerario.objects.filter(micro=patente)
	for i in itinerario:
		if(i.inicio <= hora and i.fin > hora):
			conduce = Conduce.objects.filter(itinerario = i.identificador).filter(fecha = fecha)
			if(len(conduce) != 0):
				return conduce[0].conductor
	return None
#@login_required()
def VerPerfilUsuario(request,pk):
	info_perfil = []
	try:
		us = Usuario.objects.get(rut = pk)
		info_perfil.append(us.nombre_usuario)
		info_perfil.append(us.nombre_completo)
		val = Valoracion.objects.filter(emisor=pk)
		info_perfil.append(len(val))
		#si val.size() no funciona
		#valoraciones = 0	
		#for v in val:		
		#valoraciones += 1
		#info_perfil.append(valoraciones)
	except:
		return render(request, 'perfil_error.html')
	return render(request, 'perfil_usuario.html', {'perfil': info_perfil})

def debugger(request):
	return render(request, 'registro.html', {})

def chofer_to_micro_actual(chofer):
	timezone = pytz.timezone('Chile/Continental')
	hoy = datetime.strptime(datetime.now(tz=timezone).strftime("%d/%m/%Y") , "%d/%m/%Y")
	hora = datetime.strptime(datetime.now(tz=timezone).strftime("%H") , "%H")
	conduce = Conduce.objects.filter(fecha = hoy).filter(conductor = chofer.identificador)
	for c in conduce:
		if(c.itinerario.inicio <= hora.hour and c.itinerario.fin > hora.hour):
			lol = c.itinerario.micro
			return c.itinerario.micro.patente
	return None

#@login_required()
def VerPerfilConductor(request,pk):
	info_conductor = []
	try:
		conductor = Conductor.objects.get(identificador = pk)
		info_conductor.append(conductor.nombre)
		info_conductor.append(conductor.foto)
		info_conductor.append(conductor.puntaje)
		val = Valoracion.objects.filter(receptor=pk)
		info_conductor.append(len(val))
		micro = chofer_to_micro_actual(conductor)
		if micro == None:
			info_conductor.append('---')
		else:
			info_conductor.append(chofer_to_micro_actual(conductor))
	except:
		return render(request, 'perfil_error.html')
	return render(request, 'perfil_conductor.html', {'perfil': info_conductor, 'valoraciones': val})

@csrf_exempt
def Comentar(request):
	#if post request came 
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
 
        #adding the values in a context variable 
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'comment': comment
        }
        
        #getting our showdata template
        template = loader.get_template('showdata.html')
        
        #returing the template 
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('emitir_comentario.html')
        return HttpResponse(template.render())