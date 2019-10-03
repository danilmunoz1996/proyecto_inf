from django import forms
from datetime import datetime, timedelta
import pytz

from .models import *

class ValoracionForm(forms.Form):
	puntaje = forms.NumberInput(attrs={'class':'form-control','placeholder':'Puntaje'})
	comentario = forms.CharField(label="Origen",widget=forms.TextInput(attrs={'class':'form-control'}))