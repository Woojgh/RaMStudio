from django.shortcuts import render
from grounds.models import Deck, Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy


def GroundsView(request):
    return render(request, 'grounds.html')


class GroundsDeckView(ListView):
    """Render all photos."""

    context_object_name = 'deck-photos'
    template_name = 'grounds-deck.html'
    queryset = Deck.objects.all()

    def get_context_data(self):
        context = super(GroundsDeckView, self).get_context_data()
        return context


def GroundsShopView(request):
    return render(request, 'grounds-shop.html')


# def GroundsDeckView(request):
#     return render(request, 'grounds-deck.html')


def GroundsFirepitView(request):
    return render(request, 'grounds-firepit.html')


def GroundsFrontView(request):
    return render(request, 'grounds-front.html')


def GroundsGreenhouseView(request):
    return render(request, 'grounds-greenhouse.html')


def GroundsHastaView(request):
    return render(request, 'grounds-hasta.html')


def GroundsMeditationView(request):
    return render(request, 'grounds-meditation.html')


def GroundsPondView(request):
    return render(request, 'grounds-pond.html')


def GroundsZenView(request):
    return render(request, 'grounds-zen.html')