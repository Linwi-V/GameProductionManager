from django import forms
from .models import Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class DetalleProyectoForm(forms.ModelForm):
    class Meta:
        model = DetalleProyecto
        fields = ['plataforma', 'engine', 'tamaño_equipo']
        widgets = {
            'plataforma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: PC, Mobile, Web'}),
            'engine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Unity, Godot'}),
            'tamaño_equipo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['nombre', 'tipo', 'descripcion', 'proyecto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'prioridad', 'proyecto', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }