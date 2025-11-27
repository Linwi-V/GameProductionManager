from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta
from .forms import ProyectoForm, DetalleProyectoForm, AssetForm, TareaForm, EtiquetaForm

# ========== PÁGINA DE INICIO ==========
def index(request):
    total_proyectos = Proyecto.objects.count()
    total_assets = Asset.objects.count()
    total_tareas = Tarea.objects.count()
    total_etiquetas = Etiqueta.objects.count()
    
    return render(request, 'produccion/index.html', {
        'total_proyectos': total_proyectos,
        'total_assets': total_assets,
        'total_tareas': total_tareas,
        'total_etiquetas': total_etiquetas,
    })


# ========== VISTAS DE PROYECTOS ==========
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'produccion/proyectos/lista.html', {
        'proyectos': proyectos
    })


def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'produccion/proyectos/detalle.html', {
        'proyecto': proyecto
    })


def crear_proyecto(request):
    if request.method == 'POST':
        form_proyecto = ProyectoForm(request.POST)
        form_detalle = DetalleProyectoForm(request.POST)
        
        if form_proyecto.is_valid() and form_detalle.is_valid():
            proyecto = form_proyecto.save()
            detalle = form_detalle.save(commit=False)
            detalle.proyecto = proyecto
            detalle.save()
            
            messages.success(request, 'Proyecto creado exitosamente')
            return redirect('lista_proyectos')
    else:
        form_proyecto = ProyectoForm()
        form_detalle = DetalleProyectoForm()
    
    return render(request, 'produccion/proyectos/formulario.html', {
        'form_proyecto': form_proyecto,
        'form_detalle': form_detalle,
        'titulo': 'Crear Proyecto'
    })


def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    detalle = proyecto.detalle
    
    if request.method == 'POST':
        form_proyecto = ProyectoForm(request.POST, instance=proyecto)
        form_detalle = DetalleProyectoForm(request.POST, instance=detalle)
        
        if form_proyecto.is_valid() and form_detalle.is_valid():
            form_proyecto.save()
            form_detalle.save()
            
            messages.success(request, 'Proyecto actualizado exitosamente')
            return redirect('detalle_proyecto', id=proyecto.id)
    else:
        form_proyecto = ProyectoForm(instance=proyecto)
        form_detalle = DetalleProyectoForm(instance=detalle)
    
    return render(request, 'produccion/proyectos/formulario.html', {
        'form_proyecto': form_proyecto,
        'form_detalle': form_detalle,
        'proyecto': proyecto,
        'titulo': 'Editar Proyecto'
    })


def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado exitosamente')
        return redirect('lista_proyectos')
    
    return render(request, 'produccion/confirmar_eliminacion.html', {
        'objeto': proyecto,
        'tipo': 'proyecto'
    })


# ========== VISTAS DE ASSETS ==========
def lista_assets(request):
    assets = Asset.objects.select_related('proyecto').all()
    return render(request, 'produccion/assets/lista.html', {
        'assets': assets
    })


def crear_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset creado exitosamente')
            return redirect('lista_assets')
    else:
        form = AssetForm()
    
    return render(request, 'produccion/assets/formulario.html', {
        'form': form,
        'titulo': 'Crear Asset'
    })


def editar_asset(request, id):
    asset = get_object_or_404(Asset, id=id)
    
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset actualizado exitosamente')
            return redirect('lista_assets')
    else:
        form = AssetForm(instance=asset)
    
    return render(request, 'produccion/assets/formulario.html', {
        'form': form,
        'titulo': 'Editar Asset'
    })


def eliminar_asset(request, id):
    asset = get_object_or_404(Asset, id=id)
    
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Asset eliminado exitosamente')
        return redirect('lista_assets')
    
    return render(request, 'produccion/confirmar_eliminacion.html', {
        'objeto': asset,
        'tipo': 'asset'
    })


# ========== VISTAS DE TAREAS ==========
def lista_tareas(request):
    tareas = Tarea.objects.select_related('proyecto').prefetch_related('etiquetas').all()
    return render(request, 'produccion/tareas/lista.html', {
        'tareas': tareas
    })


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea creada exitosamente')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'produccion/tareas/formulario.html', {
        'form': form,
        'titulo': 'Crear Tarea'
    })


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada exitosamente')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'produccion/tareas/formulario.html', {
        'form': form,
        'titulo': 'Editar Tarea'
    })


def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada exitosamente')
        return redirect('lista_tareas')
    
    return render(request, 'produccion/confirmar_eliminacion.html', {
        'objeto': tarea,
        'tipo': 'tarea'
    })


# ========== VISTAS DE ETIQUETAS ==========
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'produccion/etiquetas/lista.html', {
        'etiquetas': etiquetas
    })


def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    
    return render(request, 'produccion/etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Crear Etiqueta'
    })


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    
    return render(request, 'produccion/etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Editar Etiqueta'
    })


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada exitosamente')
        return redirect('lista_etiquetas')
    
    return render(request, 'produccion/confirmar_eliminacion.html', {
        'objeto': etiqueta,
        'tipo': 'etiqueta'
    })