from django.shortcuts import render


def GroundsView(request):
    return render(request, 'grounds.html')


def GroundsShopView(request):
    return render(request, 'grounds-shop.html')