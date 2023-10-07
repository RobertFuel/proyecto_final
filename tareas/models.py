from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    INGLES = 1
    FRANCES = 2
    ESPANOL = 3
    CURSO_CHOICES = [
        (INGLES, 'Inglés'),
        (FRANCES, 'Francés'),
        (ESPANOL, 'Español'),
    ]

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    curso = models.PositiveSmallIntegerField(choices=Curso.CURSO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - por ' + self.usuario.username


