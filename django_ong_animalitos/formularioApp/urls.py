from django.urls import path
from . import views


urlpatterns = [
    path('adoptame/formAdopcion/',views.formAdopcion, name='formAdopcion'),
    path('formRegistro/',views.formRegistro, name='formRegistro'), 
    path('formContacto/',views.formContacto, name='formContacto'), 
]