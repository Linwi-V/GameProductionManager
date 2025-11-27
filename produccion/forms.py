from django import forms
from datetime import date
from .models import Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta


class ProyectoForm(forms.ModelForm):
    
    #Formulario para crear y editar proyectos.
    #Incluye validación de fecha_inicio para evitar fechas en el pasado.

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del proyecto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe tu proyecto de videojuego'
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Proyecto',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha de Inicio',
            'estado': 'Estado del Proyecto'
        }
    
    def clean_nombre(self):
      
        #Valida que el nombre del proyecto tenga al menos 3 caracteres
        #y no sea solo espacios.
       
        nombre = self.cleaned_data.get('nombre')
        
        if nombre:
            nombre = nombre.strip()
            if len(nombre) < 3:
                raise forms.ValidationError(
                    'El nombre del proyecto debe tener al menos 3 caracteres.'
                )
        
        return nombre


class DetalleProyectoForm(forms.ModelForm):

    #Formulario para detalles técnicos del proyecto.
    #Incluye validación del tamaño del equipo.
    
    class Meta:
        model = DetalleProyecto
        fields = ['plataforma', 'engine', 'tamaño_equipo']
        widgets = {
            'plataforma': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PC, Mobile, Web, Consola'
            }),
            'engine': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Unity, Unreal, Godot, GameMaker'
            }),
            'tamaño_equipo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Número de personas'
            }),
        }
        labels = {
            'plataforma': 'Plataforma',
            'engine': 'Motor de Juego',
            'tamaño_equipo': 'Tamaño del Equipo'
        }
    
    def clean_tamaño_equipo(self):
      
        #Valida que el tamaño del equipo sea un número positivo razonable.
        
        tamaño = self.cleaned_data.get('tamaño_equipo')
        
        if tamaño:
            if tamaño < 1:
                raise forms.ValidationError(
                    'El tamaño del equipo debe ser al menos 1 persona.'
                )
            if tamaño > 1000:
                raise forms.ValidationError(
                    'El tamaño del equipo parece demasiado grande. Verifica el número.'
                )
        
        return tamaño


class AssetForm(forms.ModelForm):
    #Formulario para crear y editar assets del proyecto.
    
    class Meta:
        model = Asset
        fields = ['nombre', 'tipo', 'descripcion', 'proyecto']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del asset'
            }),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del asset (opcional)'
            }),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Asset',
            'tipo': 'Tipo de Asset',
            'descripcion': 'Descripción',
            'proyecto': 'Proyecto Asociado'
        }
    
    def clean_nombre(self):
        #Valida que el nombre del asset no esté vacío ni sea solo espacios.
        
        nombre = self.cleaned_data.get('nombre')
        
        if nombre:
            nombre = nombre.strip()
            if len(nombre) < 2:
                raise forms.ValidationError(
                    'El nombre del asset debe tener al menos 2 caracteres.'
                )
        
        return nombre


class TareaForm(forms.ModelForm):
    #Formulario para crear y editar tareas del proyecto.
    #Permite asignar múltiples etiquetas.
  
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'prioridad', 'proyecto', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la tarea'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe la tarea en detalle'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'titulo': 'Título de la Tarea',
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'prioridad': 'Prioridad',
            'proyecto': 'Proyecto',
            'etiquetas': 'Etiquetas'
        }
    
    def clean_titulo(self):
        #Valida que el título de la tarea tenga al menos 5 caracteres.
       
        titulo = self.cleaned_data.get('titulo')
        
        if titulo:
            titulo = titulo.strip()
            if len(titulo) < 5:
                raise forms.ValidationError(
                    'El título de la tarea debe tener al menos 5 caracteres.'
                )
        
        return titulo


class EtiquetaForm(forms.ModelForm):
    #Formulario para crear y editar etiquetas.
  
    class Meta:
        model = Etiqueta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la etiqueta'
            }),
        }
        labels = {
            'nombre': 'Nombre de la Etiqueta'
        }
    
    def clean_nombre(self):
#Valida que el nombre de la etiqueta sea único (case-insensitive)
        #y tenga un formato válido.
    
        nombre = self.cleaned_data.get('nombre')
        
        if nombre:
            nombre = nombre.strip()
            
            # Validar longitud
            if len(nombre) < 2:
                raise forms.ValidationError(
                    'El nombre de la etiqueta debe tener al menos 2 caracteres.'
                )
            
            # Validar que no exista ya (case-insensitive)
            # Excluir la instancia actual si estamos editando
            exists = Etiqueta.objects.filter(nombre__iexact=nombre)
            if self.instance.pk:
                exists = exists.exclude(pk=self.instance.pk)
            
            if exists.exists():
                raise forms.ValidationError(
                    f'Ya existe una etiqueta con el nombre "{nombre}".'
                )
        
        return nombre