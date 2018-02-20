from django.shortcuts import render


def GroundsView(request):
    return render(request, 'grounds.html')