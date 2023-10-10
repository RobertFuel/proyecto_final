from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tarea, Curso
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def obtener_curso_de_usuario(username):
    if "ingles" in username:
        return Curso.INGLES
    elif "frances" in username:
        return Curso.FRANCES
    elif "espanol" in username:
        return Curso.ESPANOL
    else:
        return None
    
def home(request):
    return render(request, 'tareas/home.html')

def es_profesor(user):
    return user.groups.filter(name='profesores').exists()

@login_required
def tareas(request):
    if request.GET.get('next') == '/tareas/crear_tarea/':
        messages.error(request, "Solo un profesor puede crear tareas.")
    
    if es_profesor(request.user):
        # Si es profesor, muestra todas las tareas que él creó
        tareas = Tarea.objects.filter(usuario=request.user, fecha_finalizacion__isnull=True)
    else:
        # Si es estudiante, muestra las tareas basadas en su "curso"
        curso_estudiante = obtener_curso_de_usuario(request.user.username)
        if curso_estudiante:
            tareas = Tarea.objects.filter(curso=curso_estudiante, fecha_finalizacion__isnull=True)
        else:
            tareas = []

    return render(request, 'tareas/tareas.html', {'tareas': tareas})

@login_required
def tareas_completadas(request):
    curso_estudiante = obtener_curso_de_usuario(request.user.username)
    
    if es_profesor(request.user):
        # Si es profesor, muestra las tareas que él creó y que han sido finalizadas
        tareas = Tarea.objects.filter(usuario=request.user, fecha_finalizacion__isnull=False).order_by('fecha_finalizacion')
    else:
        # Si es estudiante, muestra las tareas finalizadas basadas en su curso
        tareas = Tarea.objects.filter(curso=curso_estudiante, fecha_finalizacion__isnull=False).order_by('fecha_finalizacion')

    return render(request, 'tareas/tareas_completadas.html', {'tareas': tareas})

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
    curso_estudiante = obtener_curso_de_usuario(request.user.username)
    
    # Establecer cómo obtener la tarea
    if es_profesor(request.user):
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    else:
        tarea = get_object_or_404(Tarea, pk=tarea_id, curso=curso_estudiante)
    
    # Procesar el formulario
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas')
        else:
            return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': form, 'error': 'Error actualizando tarea'})
    else:
        form = TareaForm(instance=tarea)
        return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea, 'form': form})


@login_required
def completar_tarea(request, tarea_id):
    curso_estudiante = obtener_curso_de_usuario(request.user.username)
    
    # Establecer cómo obtener la tarea
    if es_profesor(request.user):
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    else:
        tarea = get_object_or_404(Tarea, pk=tarea_id, curso=curso_estudiante)
    
    if request.method == "POST":
        tarea.fecha_finalizacion = timezone.now()
        tarea.save()
        return redirect('tareas')

@login_required
def borrar_tarea(request, tarea_id):
    # Obteniendo la tarea basada en el ID, sin considerar el usuario por ahora
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    # Verifica si el usuario actual es el profesor que creó la tarea
    if not es_profesor(request.user):
        messages.error(request, "No tienes permiso para borrar esta tarea.")
        return redirect('tareas')

    if request.method == "POST":
        print("Intentando borrar tarea con ID:", tarea_id)
        tarea.delete()
        print("Tarea supuestamente borrada.")
        return redirect('tareas')


    
