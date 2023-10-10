from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from tareas.views import es_profesor

                  
def signup(request):
    
    if request.method == "GET":
        return render(request, 'usuarios/signup.html', {'form': UserCreationForm})
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
                return render(request, 'usuarios/signup.html', {
                    'form': UserCreationForm,
                    "error": "El usuario ya existe"
                })
        return render(request, 'usuarios/signup.html', {
                    'form': UserCreationForm,
                    "error": "Contraseñas no coinciden"
                })
            
        
    return render(request, 'usuarios/signup.html', {'form': UserCreationForm})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.groups.filter(name='profesores').exists():
                # Es profesor, redirigir a la página de crear tarea
                login(request, user)
                return redirect('crear_tarea')
            else:
                # Es estudiante, redirigir a la página de tareas
                login(request, user)
                return redirect('tareas')
        else:
            return render(request, 'usuarios/signin.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'usuarios/signin.html', {'form': form})

    
