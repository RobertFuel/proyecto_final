from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tarea
from django.utils import timezone

def home(request):
    return render(request, 'tareas/home.html')
                  
def signup(request):
    
    if request.method == "GET":
        return render(request, 'tareas/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'tareas/signup.html', {
                    'form': UserCreationForm,
                    "error": "El usuario ya existe"
                })
        return render(request, 'tareas/signup.html', {
                    'form': UserCreationForm,
                    "error": "Contraseñas no coinciden"
                })
            
        
    return render(request, 'tareas/signup.html', {'form': UserCreationForm})

def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_finalizacion__isnull=True)
    return render(request, 'tareas/tareas.html', {'tareas': tareas})

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

def completa_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == "POST":
        tarea.fecha_finalizacion = timezone.now()
        tarea.save()
        return redirect('tareas')

def logout_view(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == "GET":
        return render(request, 'tareas/signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'tareas/signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('tareas')
    
