from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareaForm


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
    return render(request, 'tareas/tareas.html')

def crear_tarea(request):
    return render(request, 'tareas/crear_tarea.html', {'form': TareaForm})

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
    
