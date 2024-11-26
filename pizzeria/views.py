from django.shortcuts import render, get_object_or_404 , redirect
from .models import Pizza, TipoMasa, Ingrediente,Reserva
from django.http import JsonResponse



def test(request):
    return render(request, 'index.html', {})

def portada(request):
    pizzas = Pizza.objects.all()[:3]  # Por ejemplo, las tres primeras
    return render(request, 'portada.html', {'pizzas': pizzas})

def lista_pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'lista_pizzas.html', {'pizzas': pizzas})

def detalle_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'detalle_pizza.html', {'pizza': pizza})

def lista_tipos_masa(request):
    tipos_masa = TipoMasa.objects.all()
    return render(request, 'lista_tipos_masa.html', {'tipos_masa': tipos_masa})

def detalle_tipo_masa(request, tipo_masa_id):
    tipo_masa = get_object_or_404(TipoMasa, id=tipo_masa_id)
    pizzas_asociadas = Pizza.objects.filter(tipo_masa=tipo_masa)
    return render(request, 'detalle_tipo_masa.html', {'tipo_masa': tipo_masa, 'pizzas_asociadas': pizzas_asociadas})

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'lista_ingredientes.html', {'ingredientes': ingredientes})

def detalle_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    pizzas_asociadas = Pizza.objects.filter(ingredientes=ingrediente)
    return render(request, 'pizzeria/detalle_ingrediente.html', {'ingrediente': ingrediente, 'pizzas_asociadas': pizzas_asociadas})

def formulario(request):
    if request.method == 'POST':
        
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        primera_vez = request.POST.get('primeravez') == 'si'  
        numero_comensales = request.POST.get('comensales')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        comentarios = request.POST.get('comentarios')

        
        nueva_reserva = Reserva(
            nombre=nombre,
            email=email,
            primera_vez=primera_vez,
            numero_comensales=numero_comensales,
            fecha=fecha,
            hora=hora,
            comentarios=comentarios
        )
        nueva_reserva.save()  
       
        return redirect('portada') 

    
    return render(request, 'formulario.html')




# aqui estamos verificando si hay disponibilidad de fecha y hora
def verificar_disponibilidad(request):
    fecha = request.GET.get("fecha")
    hora = request.GET.get("hora")

    if fecha and hora:
        # Contamos reservas para esa fecha y hora
        reservas = Reserva.objects.filter(fecha=fecha, hora=hora).count()
        #máximo 5 reservas por hora)
        max_reservas = 5
        disponible = reservas < max_reservas

        return JsonResponse({"disponible": disponible})

    return JsonResponse({"error": "Faltan datos de fecha y hora"}, status=400)

def lista_reservas(request):
    email_usuario = request.GET.get("email") # aqui ya tengo el correo del usuario
    reservas = Reserva.objects.filter(email=email_usuario)  # Ffiltramos las reservas por el correo
    return render(request, "lista_reservas.html", {"reservas": reservas, "email": email_usuario})



def eliminar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()  #aqui esta eliminando al reserva de la bd
        return JsonResponse({"mensaje": "Reserva cancelada con éxito."})
    except Reserva.DoesNotExist:
        return JsonResponse({"error": "Reserva no encontrada."}, status=404)