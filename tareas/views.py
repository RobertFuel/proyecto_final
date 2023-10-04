from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError


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

def logout_view(request):
    logout(request)
    return redirect('home')