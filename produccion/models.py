from django.db import models

# Modelo 1: Proyecto (entidad independiente)
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
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='planificacion')
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_inicio']
    
    def __str__(self):
        return self.nombre


# Modelo 2: DetalleProyecto (relación 1-1)
class DetalleProyecto(models.Model):
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE, related_name='detalle')
    plataforma = models.CharField(max_length=100, help_text='Ej: PC, Mobile, Web')
    engine = models.CharField(max_length=100, help_text='Ej: Unity, Godot, GameMaker')
    tamaño_equipo = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'Detalle de Proyecto'
        verbose_name_plural = 'Detalles de Proyectos'
    
    def __str__(self):
        return f"Detalle de {self.proyecto.nombre}"


# Modelo 3: Etiqueta (entidad independiente)
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


# Modelo 4: Asset (relación 1-N con Proyecto)
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
    descripcion = models.TextField(blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='assets')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


# Modelo 5: Tarea (relación 1-N con Proyecto y N-N con Etiquetas)
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
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='media')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='tareas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo