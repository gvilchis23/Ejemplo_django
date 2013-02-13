'''
Created on 12/02/2013

@author: infest48
'''
from Ejemplo_django.models import Bebida
from django.shortcuts import render_to_response

def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html',{'lista':bebidas})
