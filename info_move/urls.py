from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('ListaMicros', views.ListaMicros, name = 'ListaMicros'),
    path('ComentariosChofer', views.ComentariosChofer, name = 'ComentariosChofer'),
]