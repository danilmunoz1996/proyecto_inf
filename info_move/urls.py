from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views #Para importar un login y logout automatico de Django
from .views import *
from . import views

urlpatterns = [
	path('signup', signup, name='signup'),
    url(r'logout$', auth_views.LogoutView, {'next_page': '/home'}, name="logout"),
    path('', home, name = 'home'),
    path('ListaMicros', ListaMicros, name = 'ListaMicros'),
    path('ComentariosChofer', ComentariosChofer, name = 'ComentariosChofer'),
    #path('Comentar', Comentar, name = 'Comentar'),
   	path('valorar', CrearValoracion, name = 'CrearValoracion'),
    url(r'^usuario/(?P<pk>\d+)/$', VerPerfilUsuario, name='VerPerfilUsuario'),
    url('conductor/(?P<pk>\d+)', VerPerfilConductor, name='VerPerfilConductor'),
    path('debugger',debugger,name='debugger'),
    
    #url(r'^getdata/', views.Comentar),
    #url(r'^$', views.Comentar),
    
]