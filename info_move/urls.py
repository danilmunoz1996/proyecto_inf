from django.urls import path
from django.conf.urls import url, include
from .views import *
from . import views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
    path('', home, name = 'home'),
    path('home', home, name = 'home'),
    path('ListaMicros', ListaMicros, name = 'ListaMicros'),
    path('ComentariosChofer', ComentariosChofer, name = 'ComentariosChofer'),
    path('Comentar', Comentar, name = 'Comentar'),

    path('valorar', CrearValoracion, name = 'CrearValoracion'),
    path('busqueda_linea', SearchResultsView.as_view(), name = 'buscar_linea'),
    url(r'^usuario/(?P<pk>\d+)/$', VerPerfilUsuario, name='VerPerfilUsuario'),
    url('conductor/(?P<pk>\d+)', VerPerfilConductor, name='VerPerfilConductor'),
    url('buscador/', Buscador, name='Buscador'),
    path('debugger',debugger,name='debugger'),
    
    url(r'^getdata/', views.Comentar),
    url(r'^$', views.Comentar),
]