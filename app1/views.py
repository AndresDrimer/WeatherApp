from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):   
    texto = "in-ter-po-la-ción"
    return render (request, 'app1/public/index.html', {'texto': texto, 'hoy': datetime.now})

def quienes_somos (request):
    return render (request, 'app1/public/quienes_somos.html')


def clima_extendido (request):
    return HttpResponse ('<h4> Clima a 10 días </h4>')


def suscripcion (request, name='invitado/a'):
    return HttpResponse (f"""<h3> Desea suscribirse? </h3>
                         <p> es ud muy valiente, <strong> {name}</strong> </p>""")
    