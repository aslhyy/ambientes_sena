from django.contrib import admin
from .models import (
    Usuario,
    Ambiente,
    ItemInventario,
    Asignacion,
    HorarioAmbiente,
    Novedad
)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_usuario', 'numero_identidad', 'telefono', 'correo')
    list_filter = ('tipo_usuario',)
    search_fields = ('nombre', 'numero_identidad', 'correo')

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'capacidad', 'estado')
    list_filter = ('estado',)
    search_fields = ('codigo', 'nombre')

@admin.register(ItemInventario)
class ItemInventarioAdmin(admin.ModelAdmin):
    list_display = ('ambiente', 'tipo_item', 'cantidad_esperada', 'cantidad_actual')
    list_filter = ('tipo_item', 'ambiente')
    search_fields = ('ambiente__codigo',)

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('ambiente', 'instructor', 'fecha', 'hora_recepcion', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('ambiente__codigo', 'instructor__nombre')
    date_hierarchy = 'fecha'

@admin.register(HorarioAmbiente)
class HorarioAmbienteAdmin(admin.ModelAdmin):
    list_display = ('ambiente', 'instructor', 'dia_semana', 'hora_inicio', 'hora_fin')
    list_filter = ('dia_semana', 'ambiente')
    search_fields = ('ambiente__codigo', 'instructor__nombre', 'programa_formacion')

@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
    list_display = ('asignacion', 'descripcion', 'fecha_reporte', 'estado')
    list_filter = ('estado', 'fecha_reporte')
    search_fields = ('descripcion',)
    date_hierarchy = 'fecha_reporte'
