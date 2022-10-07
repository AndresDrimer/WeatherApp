from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):   
    return render (request, 'app1/index.html')

def quienes_somos (request):
    return HttpResponse ('<h1> Quienes somos? </h1>')

def clima_extendido (request):
    return HttpResponse ('<h4> Clima a 10 días </h4>')


def suscripcion (request, name='invitado/a'):
    return HttpResponse (f"""<h3> Desea suscribirse? </h3>
                         <p> es ud muy valiente, <strong> {name}</strong> </p>""")