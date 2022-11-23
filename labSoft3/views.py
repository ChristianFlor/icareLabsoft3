from django.shortcuts import render
from.models import reserva
def metzli(request):
    return render(request, 'icare/MEZTLI.html')

def menu(request):
    return render(request, 'icare/menu.html')

def sugerencias(request):
    return render(request, 'icare/sugerencia.html')