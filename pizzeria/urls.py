from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    
    path('', views.portada, name='portada'),
    path('pizzas/', views.lista_pizzas, name='lista_pizzas'),
    path('pizzas/<int:pizza_id>/', views.detalle_pizza, name='detalle_pizza'),
    path('tipos_masa/', views.lista_tipos_masa, name='lista_tipos_masa'),
    path('tipos_masa/<int:tipo_masa_id>/', views.detalle_tipo_masa, name='detalle_tipo_masa'),
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/<int:ingrediente_id>/', views.detalle_ingrediente, name='detalle_ingrediente'),
    path('formulario/', views.formulario, name='formulario'), 
    path("verificar-disponibilidad/", views.verificar_disponibilidad, name="verificar_disponibilidad"),
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("eliminar-reserva/<int:id>/", views.eliminar_reserva, name="eliminar_reserva"),
]