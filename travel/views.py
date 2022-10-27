from django.shortcuts import render
from .models import Place


def home(request):
    context = {
        'title': 'Home',
        'places': Place.objects.all()
    }
    return render(request, 'travel/home.html', context)


def international(request):
    context = {
        'title': 'International',
        'places': Place.objects.filter(category='IN')
    }
    return render(request, 'travel/places.html', context)


def domestic(request):
    context = {
        'title': 'Domestic',
        'places': Place.objects.filter(category='DM')
    }
    return render(request, 'travel/places.html', context)
