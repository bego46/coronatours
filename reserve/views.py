from ssl import AlertDescription
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Reserver, Destination, Vehiculos, Zone
import locale


# ----- Create your views here. -----


def reserve(request):

    destination = Destination.objects.all()

    return render(request, 'reserve.html', {
        'title': 'Reservas',
        'destination': destination,
    })


def det_reserve(request):

    if request.method == 'POST':
        # >>>>>>>--- comente unas variables por aqui ---<<<<<<<
        # ----- Declaracion de variables -----
        # transports = Vehiculos.objects.all()
        # destination = Destination.objects.all()
        start_of_route = request.POST['start_of_route']
        end_of_route = request.POST['end_of_route']
        date = request.POST['date']
        time = request.POST['time']
        duration = request.POST['duration']


        # reserve = Reserver(
        #     start_and_route=start_of_route,
        #     end_and_route=end_of_route,
        #     date=date,
        #     hour=time
        # )

        # reserve.save()
        # d_reserve = Reserver.objects.all()

    return render(request, 'det_reser.html', {
        'title': 'Detalles Reservas',
        # 'd_reserve': d_reserve,
        # 'zonas': zona,
        'start_of_route': start_of_route,
        'end_of_route': end_of_route,
        'date': date,
        'time': time,
        "duration": duration
    })


def transporte(request):

    if request.method == 'POST':

        zona = Zone.objects.all()
        transports = Vehiculos.objects.all()
        destination = Destination.objects.all()

        start_of_route = request.POST['start_of_route']
        end_of_route = request.POST['end_of_route']
        # name  = request.POST['name']
        # email = request.POST['mail']
        # tel  = request.POST['tel']
        date = request.POST['date']
        time = request.POST['time']
        distance = request.POST['distance']
        duration = request.POST['duration']
        store = request.POST['store']

        # id_POST  = request.POST['id']

        # ----- Aqui se guradan los datos ingresados en el formulario de reserva -----

        # reserve = Reserver(
        #     # fullname = name,
        #     # email = email,
        #     # phone = tel,
        #     start_and_route=start_of_route,
        #     end_and_route=end_of_route,
        #     date=date,
        #     hour=time
        # )

        # reserve.save()
        # d_reserve = Reserver.objects.all()
        st_distancia = int(store)*10**-3;
        print(round(st_distancia))
        kilometros = int(round(st_distancia))

        if int(kilometros) in range(1, 12):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'compartido': 10000,  # multiplicar por personas
                'standar': locale.currency(45000, grouping=True),
                'mini_van': locale.currency(85000, grouping=True),
                'van_standar': locale.currency(100000, grouping=True),
                'micro_bus': locale.currency(120000, grouping=True),
                'buseta': locale.currency(170000, grouping=True),
                'bus': locale.currency(200000, grouping=True),
                'SUV': locale.currency(150000, grouping=True),
            }
        elif int(kilometros) in range(13, 30):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'compartido': 10000,
                'standar': locale.currency(60000, grouping=True),
                'mini_van': locale.currency(100000, grouping=True),
                'van_standar': locale.currency(120000, grouping=True),
                'micro_bus': locale.currency(150000, grouping=True),
                'buseta': locale.currency(190000, grouping=True),
                'bus': locale.currency(260000, grouping=True),
                'SUV': locale.currency(180000, grouping=True),
            }
        elif int(kilometros) in range(31, 58):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'compartido': locale.currency(10000, grouping=True),
                'standar': locale.currency(190000, grouping=True),
                'mini_van': locale.currency(280000,  grouping=True),
                'van_standar': locale.currency(400000, grouping=True),
                'micro_bus': locale.currency(480000, grouping=True),
                'buseta': locale.currency(530000, grouping=True),
                'bus': locale.currency(600000, grouping=True),
                'SUV': locale.currency(500000, grouping=True),
            }
        else:
            print("Incorrecto")

        return render(request, 'transporte.html', {
            # >>>>>>>--- comente unas variables por aqui ---<<<<<<<
            'title': 'Transporte',
            'transports': transports,
            # 'destinations': destino,
            # 'd_reserve': d_reserve,
            'v_trayecto': valor_trayecto,
            'zonas': zona,
            'start_of_route': start_of_route,
            'end_of_route': end_of_route,
            "distance": distance,
            "duration": duration,
            'date': date,
            'time': time,
            'store': store
        })
    else:
        return HttpResponse("No se guardo ninguna informacion vuelva a <a href='/inicio'>Inicio</a> ")
