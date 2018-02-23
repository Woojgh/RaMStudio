from django.shortcuts import render


def GroundsView(request):
    return render(request, 'grounds.html')


def GroundsShopView(request):
    return render(request, 'grounds-shop.html')


def GroundsDeckView(request):
    return render(request, 'grounds-deck.html')


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