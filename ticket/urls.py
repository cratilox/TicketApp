from django.contrib import admin
from django.urls import path
from . import views
from .views import ticket_detalle, reserva_ticket


urlpatterns = [
    path('consulta_ticket/', views.consulta_ticket, name='consulta_ticket'),
    path('add_ticket', views.TicketCreate.as_view(), name="add_ticket"),
    path('formulariotickets', views.formulariotickets, name='formulariotickets' ),

    path('add_ticket', views.TicketCreate.as_view(), name="add_ticket"),
    
    path('edit_ticket/<int:pk>', views.TicketUpdate.as_view(), name='edit_ticket'),
    
    path('list_ticket', views.TicketList.as_view(), name="list_ticket"),
    
    path('del_ticket/<int:pk>', views.TicketDelete.as_view(), name="del_ticket"),
    

    # ==== Funciones para el reservado de tickets

    path('ticket/<uuid:numero_ticket>/', ticket_detalle, name='ticket_detalle'),
    path('reserva/<uuid:numero_ticket>/', reserva_ticket, name='reserva_ticket'),
]