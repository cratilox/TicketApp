from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.iniciar_sesion, name='login'),
    path("cuenta/", views.cuenta, name="cuenta"),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path("delete-card/<int:id>", views.deleteCard, name="deleteCard")
]
