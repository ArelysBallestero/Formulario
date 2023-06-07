from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenida (request):
    print ('Hola')
    return HttpResponse( 'Hola')