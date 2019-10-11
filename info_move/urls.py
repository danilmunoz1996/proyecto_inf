from django.urls import path
from django.conf.urls import url, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
	path('signup', signup, name='signup'),
    url(r'login$', LoginView.as_view(template_name='login.html',extra_context={
            'next': '/buscador'}), name="login"),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': 'home'}, name="logout"),
    path('', home, name = 'home'),
    path('ListaMicros', ListaMicros, name = 'ListaMicros'),
    path('ComentariosChofer', ComentariosChofer, name = 'ComentariosChofer'),
    #path('Comentar', Comentar, name = 'Comentar'),
    path('valorar', CrearValoracion, name = 'CrearValoracion'),
    path('busqueda_linea', SearchResultsView.as_view(), name = 'buscar_linea'),
    url(r'^usuario/(?P<pk>\d+)/$', VerPerfilUsuario, name='VerPerfilUsuario'),
    url('conductor/(?P<pk>\d+)', VerPerfilConductor, name='VerPerfilConductor'),
    url('buscador/', Buscador, name='Buscador'),
    path('debugger',debugger,name='debugger'),
    
    #url(r'^getdata/', views.Comentar),
    #url(r'^$', views.Comentar),
    
]