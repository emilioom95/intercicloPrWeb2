from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def nuevo_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'libros/nuevo_libro.html', {'form': form})
