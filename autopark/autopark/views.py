from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages


def pagina1(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina1.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

def pagina2(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina2.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

def pagina3(request):
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

def pagina4(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina4.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

def pagina5(request):
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

def pagina6(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/ver_mas.html")
    #cargar el documento en una variable de tipo Template
    templates=Template(plantillaExterna.read())
    #cerramos el documento
    plantillaExterna.close()
    #creamos un contexto
    contexto=Context()
    #renderizamos la plantilla
    docuemnto = templates.render(contexto)
    return HttpResponse(docuemnto)

def contact_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if email and mensaje:
            send_mail(
                subject="Nuevo mensaje de contacto",
                message=f"De: {email}\n\n{mensaje}",
                from_email=email,
                recipient_list=["xciclos@gmail.com"],  # Tu correo personal
                fail_silently=False,
            )
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("contacto")  # Redirige a la misma página o a una de confirmación
        
        messages.error(request, "Todos los campos son obligatorios.")

    return render(request, "pagina5.html")  # Renderiza la página de contacto