from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('nuevo/', views.nuevo_libro, name='nuevo_libro'),
]