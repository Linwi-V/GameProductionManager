from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.index, name='index'),

    # Proyectos
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/<int:id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyectos/<int:id>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Assets
    path('assets/', views.lista_assets, name='lista_assets'),
    path('assets/crear/', views.crear_asset, name='crear_asset'),
    path('assets/<int:id>/editar/', views.editar_asset, name='editar_asset'),
    path('assets/<int:id>/eliminar/', views.eliminar_asset, name='eliminar_asset'),

    # Tareas
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),

    # Etiquetas
    path('etiquetas/', views.lista_etiquetas, name='lista_etiquetas'),
    path('etiquetas/crear/', views.crear_etiqueta, name='crear_etiqueta'),
    path('etiquetas/<int:id>/editar/', views.editar_etiqueta, name='editar_etiqueta'),
    path('etiquetas/<int:id>/eliminar/', views.eliminar_etiqueta, name='eliminar_etiqueta'),
]
