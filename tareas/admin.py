from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_finalizacion')

admin.site.register(Tarea, TareaAdmin)
