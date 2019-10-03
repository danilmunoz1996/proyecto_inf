from django import forms
from datetime import datetime, timedelta
import pytz

from .models import *

class ValoracionForm(forms.Form):
	patente = forms.CharField(label="Patente",min_length=6,max_length=6,widget=forms.TextInput(attrs={'class':'form-control'}))
	puntaje = forms.IntegerField(min_value=1,max_value=5)
	comentario = forms.CharField(label="Comentario",widget=forms.TextInput(attrs={'class':'form-control'}))