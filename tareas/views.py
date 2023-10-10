from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'tareas/home.html')

def es_profesor(user):
    return user.groups.filter(name='Profesores').exists()

@login_required
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_finalizacion__isnull=True)
    return render(request, 'tareas/tareas.html', {'tareas': tareas})

@login_required
def tareas_completadas(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_finalizacion__isnull=False).order_by('fecha_finalizacion')
    return render(request, 'tareas/tareas.html', {'tareas': tareas})

@login_required
@user_passes_test(es_profesor, login_url='tareas')
def crear_tarea(request):
    
    if request.method == "GET":
        return render(request, 'tareas/crear_tarea.html', {'form': TareaForm})
    else:
        try:
            form = TareaForm(request.POST)
            new_tarea = form.save(commit=False)
            new_tarea.usuario = request.user
            new_tarea.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tareas/crear_tarea.html', {'form': TareaForm, 'error': 'Faltan datos'})
        
@login_required
def detalle_tarea(request, tarea_id):
    if request.method == "GET":
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
        form = TareaForm(instance=tarea)
        return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': form})
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': TareaForm, 'error': 'Error actualizando tarea'})

@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == "POST":
        tarea.fecha_finalizacion = timezone.now()
        tarea.save()
        return redirect('tareas')

@login_required
def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == "POST":
        tarea.delete()
        return redirect('tareas')

    
