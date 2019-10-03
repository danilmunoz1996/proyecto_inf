from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'index.html')

def ListaMicros(request):
	return render(request, 'Lista.html')

def ComentariosChofer(request):
	return render(request, 'CometariosChofer.html')