from django.http import HttpResponse
from django.template import Template, Context
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render


def pagina1(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/pagina1.html", encoding="utf-8")
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
    plantillaExterna=open("autopark/templates/pagina2.html", encoding="utf-8")
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
    plantillaExterna=open("autopark/templates/pagina3.html", encoding="utf-8")
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
    plantillaExterna=open("autopark/templates/pagina4.html", encoding="utf-8")
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
    return render(request, "pagina5.html")


def pagina6(request):
    #abrimos un docuemnto que contiene la plantilla html
    plantillaExterna=open("autopark/templates/ver_mas.html", encoding="utf-8")
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
        email = request.POST.get("email")  # Correo del usuario
        mensaje = request.POST.get("mensaje")
        
        if email and mensaje:
            try:
                # Usa tu cuenta de Gmail configurada como remitente
                send_mail(
                    subject="Nuevo mensaje de contacto",
                    message=f"Mensaje enviado por: {email}\n\n{mensaje}",
                    from_email="xciclos@gmail.com",  # Debe ser el mismo que EMAIL_HOST_USER
                    recipient_list=["xciclos@gmail.com"],  # Destinatario
                    fail_silently=False,
                    encoding='utf-8',
                )
                messages.success(request, "Tu mensaje ha sido enviado con éxito.")
                return redirect("contacto")
            except Exception as e:
                messages.error(request, f"Hubo un error al enviar el mensaje: {e}")
        else:
            messages.error(request, "Todos los campos son obligatorios.")
    
    return render(request, "pagina5.html")
