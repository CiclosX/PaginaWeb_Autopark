from django.http import HttpResponse
from django.template import Template, Context


def home(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("C:/Users/Usuario/Desktop/autopark/integradora/templates/home.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

