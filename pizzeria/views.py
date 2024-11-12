from django.shortcuts import render, get_object_or_404
from .models import Pizza, TipoMasa, Ingrediente

def portada(request):
    pizzas = Pizza.objects.all()[:3]  # Por ejemplo, las tres primeras
    return render(request, 'pizzeria/portada.html', {'pizzas': pizzas})

def lista_pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzeria/lista_pizzas.html', {'pizzas': pizzas})

def detalle_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'pizzeria/detalle_pizza.html', {'pizza': pizza})

def lista_tipos_masa(request):
    tipos_masa = TipoMasa.objects.all()
    return render(request, 'pizzeria/lista_tipos_masa.html', {'tipos_masa': tipos_masa})

def detalle_tipo_masa(request, tipo_masa_id):
    tipo_masa = get_object_or_404(TipoMasa, id=tipo_masa_id)
    pizzas_asociadas = Pizza.objects.filter(tipo_masa=tipo_masa)
    return render(request, 'pizzeria/detalle_tipo_masa.html', {'tipo_masa': tipo_masa, 'pizzas_asociadas': pizzas_asociadas})

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'pizzeria/lista_ingredientes.html', {'ingredientes': ingredientes})

def detalle_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    pizzas_asociadas = Pizza.objects.filter(ingredientes=ingrediente)
    return render(request, 'pizzeria/detalle_ingrediente.html', {'ingrediente': ingrediente, 'pizzas_asociadas': pizzas_asociadas})

def formulario (request):
    return render(request, 'pizzeria/formulario.html', {'formulario':None})