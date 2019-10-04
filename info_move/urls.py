from django.urls import path
from django.conf.urls import url, include
from .views import * 
urlpatterns = [
    path('', home, name = 'home'),
    path('ListaMicros', ListaMicros, name = 'ListaMicros'),
    path('ComentariosChofer', ComentariosChofer, name = 'ComentariosChofer'),
    path('valorar', CrearValoracion, name = 'CrearValoracion'),
    path('busqueda_linea', SearchResultsView.as_view(), name = 'buscar_linea'),
    url(r'^usuario/(?P<pk>\d+)/$', VerPerfilUsuario, name='VerPerfilUsuario'),
    url('conductor/(?P<pk>\d+)', VerPerfilConductor, name='VerPerfilConductor'),
    path('debugger',debugger,name='debugger'),
]