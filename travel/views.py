from django.shortcuts import render
from .models import Place, PlacesToVisit
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'title': 'Home',
        'places': Place.objects.all()
    }
    return render(request, 'travel/home.html', context)


class PlaceListView(ListView):
    model = Place
    template_name = 'travel/home.html'
    context_object_name = 'places'
    ordering = ['name']


def details(request, pk):
    context = {
        'title': 'Details',
        'places_to_visit': PlacesToVisit.objects.filter(place=Place.objects.filter(id=pk)[0])
    }
    return render(request, 'travel/place_details.html', context)


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


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'travel/about.html', context)
