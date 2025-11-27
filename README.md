# Game Production Manager

Sistema de gestión de proyectos de videojuegos desarrollado con Django que permite a los usuarios administrar proyectos, assets, tareas y etiquetas de manera eficiente y organizada.

![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## Descripción del Proyecto

Este proyecto forma parte de la **Evaluación de Portafolio del Módulo 7** del Bootcamp Desarrollo Full Stack de Python. Implementa un sistema completo de gestión de producción de videojuegos con operaciones CRUD, validación de formularios, relaciones entre modelos y una interfaz moderna y responsiva.

## Características Principales

### Gestión de Proyectos

* Crear nuevos proyectos con información detallada (nombre, descripción, fechas, estado)
* Gestión de detalles técnicos (plataforma, engine, tamaño del equipo)
* Visualización en cards modernas con estadísticas en tiempo real
* Vista de detalle con assets y tareas asociadas
* Edición y eliminación con confirmación de seguridad

### Gestión de Assets

* Crear, editar y eliminar assets vinculados a proyectos
* Clasificación por tipo: Sprite, Audio, Música, Modelo 3D, Otro
* Iconos visuales diferenciados por tipo de asset
* Asociación directa con proyectos específicos

### Gestión de Tareas y Etiquetas

* Sistema completo de tareas con prioridades (Baja, Media, Alta)
* Estados de seguimiento (Pendiente, En Proceso, Completada)
* Sistema de etiquetas para categorización flexible
* Relaciones muchos a muchos entre tareas y etiquetas
* Badges de colores para identificación visual rápida

### Seguridad y Validación

* Validación completa mediante Django Forms
* Protección CSRF en todos los formularios
* Uso de `get_object_or_404` para manejo seguro de errores
* Mensajes informativos de éxito y error al usuario
* Templates de confirmación para acciones críticas

### Interfaz de Usuario Moderna

* Diseño responsivo con Bootstrap 5.3 y CSS personalizado
* Gradientes modernos en navbar y hero section
* Cards con animaciones hover y transiciones suaves
* Iconos de Bootstrap Icons en toda la aplicación
* Paleta de colores profesional y coherente
* Sistema de templates con herencia para código DRY
* Estadísticas visuales en dashboard principal

## Tecnologías Utilizadas

* **Backend:** Python 3.12 + Django 5.2.7
* **Frontend:** HTML5, CSS3 (custom), Bootstrap 5.3
* **Base de Datos:** MySQL 8.0
* **Iconos:** Bootstrap Icons 1.10.5
* **Tipografía:** Google Fonts (Inter)
* **Control de versiones:** Git / GitHub

## Arquitectura del Proyecto

El proyecto sigue el patrón **MVT (Model-View-Template)** de Django:

* **Models:** Definición de entidades (Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta)
* **Views:** Lógica de negocio para operaciones CRUD
* **Templates:** Interfaces HTML dinámicas con herencia
* **Forms:** Validación y procesamiento de datos de usuario
* **Admin:** Panel de administración personalizado de Django

## Requisitos Previos

* Python 3.8 o superior
* pip (gestor de paquetes de Python)
* MySQL 8.0 o superior
* Git

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Linwi-V/GameProductionManager.git
cd game_production
```

### 2. Crear y activar entorno virtual

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**En Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Asegúrate de tener MySQL corriendo y configura las credenciales en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'game_production_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

### 8. Acceder a la aplicación

* **Aplicación principal:** http://127.0.0.1:8000/
* **Panel de administración:** http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
game_production/
├── manage.py
├── requirements.txt
├── README.md
├── game_production/              # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── produccion/                   # Aplicación principal
    ├── models.py                 # Modelos de datos
    ├── views.py                  # Lógica de vistas CRUD
    ├── urls.py                   # Rutas de la aplicación
    ├── forms.py                  # Formularios Django
    ├── admin.py                  # Configuración del panel admin
    ├── static/
    │   └── produccion/
    │       └── css/
    │           └── styles.css    # Estilos personalizados
    └── templates/
        └── produccion/
            ├── base.html         # Template base
            ├── index.html        # Dashboard principal
            ├── confirmar_eliminacion.html
            ├── proyectos/
            │   ├── lista.html
            │   ├── formulario.html
            │   └── detalle.html
            ├── assets/
            │   ├── lista.html
            │   └── formulario.html
            ├── tareas/
            │   ├── lista.html
            │   └── formulario.html
            └── etiquetas/
                ├── lista.html
                └── formulario.html
```

## Funcionalidades Técnicas Implementadas

### Sistema de Modelos

* Relaciones **Uno a Uno** (Proyecto - DetalleProyecto)
* Relaciones **Uno a Muchos** (Proyecto - Assets, Proyecto - Tareas)
* Relaciones **Muchos a Muchos** (Tareas - Etiquetas)
* Uso de `ForeignKey`, `OneToOneField` y `ManyToManyField`

### Sistema de Vistas

* Vistas basadas en funciones (FBV)
* Operaciones CRUD completas para todas las entidades
* Manejo de formularios con validación
* Sistema de mensajes de feedback al usuario
* Protección con `get_object_or_404`

### Sistema de Templates

* Herencia de templates con `base.html`
* Uso de bloques dinámicos (`{% block %}`)
* Carga de archivos estáticos con `{% static %}`
* Iteración con `{% for %}` y condicionales `{% if %}`
* Filtros de Django (`truncatewords`, `date`, etc.)

### Migraciones

* Creación y aplicación de migraciones con `makemigrations` y `migrate`
* Propagación de cambios en el esquema de base de datos
* Manejo de relaciones entre tablas

### ORM de Django

* Consultas con `objects.all()`, `objects.count()`
* Uso de `select_related()` y `prefetch_related()` para optimización
* Filtrado y ordenamiento de datos
* Métodos personalizados en modelos

### Panel de Administración

* Configuración personalizada con `admin.py`
* Registro de todos los modelos
* Interfaz para gestión rápida de datos

## Aprendizajes Clave

* Arquitectura MVT (Model-View-Template) de Django
* Implementación completa de operaciones CRUD
* Validación de datos con Django Forms
* Manejo de relaciones entre modelos (1-1, 1-N, N-M)
* Sistema de templates con herencia
* Integración de Bootstrap con Django
* Optimización de consultas con ORM
* Diseño de interfaces modernas con CSS personalizado
* Buenas prácticas de seguridad web
* Control de versiones con Git

## Autor

**Linwi Vargas** - Productor de Videojuegos Junior

* GitHub: [@Linwi-V](https://github.com/Linwi-V)
* LinkedIn: [Linwi Vargas Campos](https://www.linkedin.com/in/linwi-vargas)
* Itch.io: [linwi.itch.io](https://linwi.itch.io)

## Proyecto Académico

Proyecto desarrollado como parte del **Bootcamp de Desarrollo Full Stack Python** - Evaluación de Portafolio del Módulo 7.

## Licencia

Este proyecto es de uso educativo como parte del portafolio de aprendizaje.
