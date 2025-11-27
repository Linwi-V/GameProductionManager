from django.db import models


# Proyecto es el modelo principal donde guardamos toda la info básica del juego
# Se relaciona con DetalleProyecto (1 a 1), Assets (1 a muchos) y Tareas (1 a muchos)
class Proyecto(models.Model):
    
    ESTADO_CHOICES = [
        ('planificacion', 'Planificación'),
        ('desarrollo', 'En Desarrollo'),
        ('testing', 'Testing'),
        ('finalizado', 'Finalizado'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='planificacion'
    )
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_inicio']  # Los más recientes primero
    
    def __str__(self):
        return self.nombre


# DetalleProyecto guarda info técnica extra del proyecto
# Relación 1:1 - cada proyecto tiene solo un detalle
class DetalleProyecto(models.Model):
    
    # Si se elimina el proyecto, se elimina el detalle también (CASCADE)
    proyecto = models.OneToOneField(
        Proyecto, 
        on_delete=models.CASCADE, 
        related_name='detalle'
    )
    plataforma = models.CharField(
        max_length=100, 
        help_text='Ej: PC, Mobile, Web'
    )
    engine = models.CharField(
        max_length=100, 
        help_text='Ej: Unity, Godot, GameMaker'
    )
    tamaño_equipo = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'Detalle de Proyecto'
        verbose_name_plural = 'Detalles de Proyectos'
    
    def __str__(self):
        return f"Detalle de {self.proyecto.nombre}"


# Etiquetas para categorizar tareas - modelo independiente
# Se pueden usar cosas como "Bug", "Feature", "Arte", "Sonido", etc.
class Etiqueta(models.Model):
    
    nombre = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']  # Orden alfabético
    
    def __str__(self):
        return self.nombre


# Asset representa cualquier recurso del proyecto: sprites, audio, modelos 3D, etc.
# Relación N:1 con Proyecto - un proyecto puede tener muchos assets
class Asset(models.Model):
    
    TIPO_CHOICES = [
        ('sprite', 'Sprite/Gráfico'),
        ('audio', 'Audio/SFX'),
        ('musica', 'Música'),
        ('modelo3d', 'Modelo 3D'),
        ('otro', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True)  # Opcional
    
    # Si se elimina el proyecto, se eliminan todos sus assets (CASCADE)
    proyecto = models.ForeignKey(
        Proyecto, 
        on_delete=models.CASCADE, 
        related_name='assets'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se guarda automáticamente
    
    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        ordering = ['-fecha_creacion']  # Los más nuevos primero
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


# Tarea representa trabajo pendiente en un proyecto
# Relación N:1 con Proyecto y N:M con Etiquetas
class Tarea(models.Model):
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='pendiente'
    )
    prioridad = models.CharField(
        max_length=20, 
        choices=PRIORIDAD_CHOICES, 
        default='media'
    )
    
    # Si se elimina el proyecto, se eliminan todas sus tareas (CASCADE)
    proyecto = models.ForeignKey(
        Proyecto, 
        on_delete=models.CASCADE, 
        related_name='tareas'
    )
    
    # Una tarea puede tener muchas etiquetas y viceversa (N:M)
    etiquetas = models.ManyToManyField(
        Etiqueta, 
        blank=True,  # No es obligatorio tener etiquetas
        related_name='tareas'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-fecha_creacion']  # Las más recientes primero
    
    def __str__(self):
        return self.titulo