from django.contrib import admin
from .models import Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'fecha_inicio', 'contar_assets', 'contar_tareas')
    list_filter = ('estado', 'fecha_inicio')
    search_fields = ('nombre', 'descripcion')
    
    def contar_assets(self, obj):
        return obj.assets.count()
    contar_assets.short_description = 'Assets'
    
    def contar_tareas(self, obj):
        return obj.tareas.count()
    contar_tareas.short_description = 'Tareas'

@admin.register(DetalleProyecto)
class DetalleProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'plataforma', 'engine', 'tamaño_equipo')
    search_fields = ('proyecto__nombre', 'plataforma', 'engine')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'proyecto', 'fecha_creacion')
    list_filter = ('tipo', 'proyecto', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'prioridad', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'proyecto', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    filter_horizontal = ('etiquetas',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contar_tareas')
    search_fields = ('nombre',)
    
    def contar_tareas(self, obj):
        return obj.tareas.count()
    contar_tareas.short_description = 'Tareas'
