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
<<<<<<< HEAD

=======
    path('formulario/', views.formulario, name='formulario'), 
>>>>>>> 0f5698b9d76f8f76f2fbe15a49ec865bb6bfae67
]