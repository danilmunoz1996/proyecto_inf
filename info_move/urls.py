from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('ListaConductores', views.ListaConductores, name = 'ListaConductores'),
    path('valorar', views.crear_valoracion, name = 'crear_valoracion'),
]