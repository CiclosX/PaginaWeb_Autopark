from django.contrib import admin
from django.urls import path
from autopark.views import pagina1, pagina2, pagina3, pagina4, pagina5, pagina6
from .views import contact_view

urlpatterns = [
    path('', pagina1, name='home'),
    path('pagina1/', pagina1, name='pagina1'),
    path('pagina2/', pagina2, name='pagina2'),
    path('pagina3/', pagina3, name='pagina3'),
    path('pagina4/', pagina4, name='pagina4'),
    path('pagina5/', pagina5, name='pagina5'),
    path('pagina6/', pagina6, name='pagina6'),
    path('contacto/', contact_view, name='contacto'),
]

