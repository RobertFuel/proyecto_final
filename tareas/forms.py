from django import forms
from .models import Tarea, Curso

class TareaForm(forms.ModelForm):
    # Agrega el campo de selección para el curso
    curso = forms.ChoiceField(choices=Curso.CURSO_CHOICES, label='Curso')

    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'curso', 'importante']
