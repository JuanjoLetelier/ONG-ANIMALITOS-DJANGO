from django.urls import path
from . import views

urlpatterns = [
    path('carritoAdopcion/', views.carritoAdopcion, name='carritoAdopcion'),
]