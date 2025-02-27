from django.http import HttpResponse
from django.template import Template, Context

def hello (request):
    return HttpResponse("Hola Mundo")


def page3(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina3.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

def page5(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina5.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

