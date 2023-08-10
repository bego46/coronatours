from django.shortcuts import render, HttpResponse
from .models import Tours

# Create your views here.

def tours(request):

    toures = Tours.objects.all()

    return render(request, 'toures.html', {
        'title': 'Toures',
        'toures': toures
    })

    # return HttpResponse("<h1>Toures</h1>")

def tour(request):
    return render(request, 'toures.html', {
        'title': 'Toures'
    })


def tour(request, id):

    tours = Tours.objects.get(id=id)
   
    return render(request, 'tour.html', {
        'title': 'San Basilio de Palenque ',
        'tours': tours 
    })