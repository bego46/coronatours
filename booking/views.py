from django.shortcuts import render, get_object_or_404
from tours.models import Tours
from reserve.models import Reserver
from .models import Booking

# Create your views here.


def check(request, id=False):
    d_reserve = Reserver.objects.all()

    if id == False and request.method == 'POST':
        # det_booking = get_object_or_404(Reserver, pk=id)

        if request.POST['name'] == "Mercedes Sprinter":
            print("Es compartido ")
            det_booking = {
                "name": request.POST['name'],
                "origen": request.POST['origen'],
                "destino": request.POST['destino'],
                "date": request.POST['date'],
                "time": request.POST['time'],
                "opcion": "transporte"
            }

            can_comp = request.POST['comp-cantidad']
            cash = request.POST['value']
            cash = int(can_comp) * int(cash)

            print(cash)

        else:
            print("no es compartido")

            det_booking = {
                "name": request.POST['name'],                
                "origen": request.POST['origen'],
                "destino": request.POST['destino'],
                "date": request.POST['date'],
                "time": request.POST['time'],
                "opcion": "transporte"
            }
            print("Este es la hora actual" + str(det_booking['time']))

            segmentar = list(det_booking['time'])           
            hora_val = segmentar[0] + segmentar[1]
            print("hora dividido" + hora_val)

            if int(hora_val) in range(22, 24) or int(hora_val) in range(0, 6) :
                cash = int(request.POST['value']) + 20000
                print("Se esta enviando este, hora nocturna ")
                print(cash)
            else:
                cash = request.POST['value']
                print("Se esta enviando este, hora diurna ")
       
    else:
        det_booking = get_object_or_404(Tours, pk=id)
        print(det_booking)

        # print(tour.cash)
    return render(request, 'check.html', {
        'title': 'Informacion de reserva',
        'det_booking': det_booking,
        'd_reserve': d_reserve,
        'cash': cash
    })


def det_booking(request, opc):

    tour = Tours.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        mail = request.POST['mail']
        contry = request.POST['contry']
        city = request.POST['city']
        cash = request.POST['cash']
        tour = request.POST['tour']
        adults = request.POST['adults']
        childre = request.POST['childre']
        option = request.POST['opcion']
        aerolinea = request.POST['aerolinea']
        nvuelo = request.POST['nvuelo']

        # if request.POST['hotel'] != "transporte":
        #     hotel  = request.POST['hotel']

        total = int(adults) * int(cash)

    booking = Booking(
        name=name,
        lastname=lastname,
        phone=phone,
        mail=mail,
        contry=contry,
        city=city,
        # hotel  = hotel,
        cash=cash,
        tour=tour,
        adults=adults,
        childre=childre,
        total=total,
        air=aerolinea,
        nair=nvuelo
    )

    booking.save()

    if option == "transporte":
        opcion = "transporte"

    return render(request, 'det_booking.html', {
        'title': 'Detalles de Reserva',
        'total': total,
        'booking': booking,
        'opcion': opcion
    })


def answer_booking(request, id):
    return render(request, 'respuesta.html',{
        'tiitle': 'confirmacion de reserva',
        'id': id
    })
