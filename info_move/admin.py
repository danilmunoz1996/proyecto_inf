from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    #A form for creating new users. Includes all the required
    #fields, plus a repeated password.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('correo', 'nombre_usuario', 'nombre_completo', 'rut')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
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