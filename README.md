
# Game Production Manager - Django Framework

Sistema de gestión de proyectos de videojuegos desarrollado con Django que permite a los usuarios administrar proyectos, assets, tareas y etiquetas de manera eficiente y organizada.

## Descripción del Proyecto

Este proyecto forma parte de la Evaluación de Portafolio del Módulo 7 del Bootcamp Desarrollo Full Stack de Python. Permite crear, visualizar, editar y eliminar proyectos, assets, tareas y etiquetas. Se implementan funcionalidades completas de CRUD, validación de formularios y navegación con templates heredados, siguiendo las buenas prácticas del framework Django.

## Características Principales

### Gestión de Proyectos

* Crear nuevos proyectos con nombre, descripción, fechas, estado y detalle del proyecto (plataforma, engine, tamaño del equipo).
* Visualizar lista completa de proyectos con información resumida.
* Ver detalle de cada proyecto junto con sus assets y tareas asociados.
* Editar proyectos existentes.
* Eliminar proyectos con confirmación.

### Gestión de Assets

* Crear, editar y eliminar assets asociados a proyectos.
* Visualizar assets relacionados a cada proyecto.
* Clasificación de assets por tipo (sprite, audio, música, 3D, otro).

### Gestión de Tareas y Etiquetas

* Crear, editar y eliminar tareas asociadas a proyectos.
* Gestionar etiquetas y asociarlas a tareas.
* Visualizar tareas por proyecto y sus etiquetas correspondientes.
* Seguimiento del estado y prioridad de las tareas.

### Seguridad y Validación

* Validación de datos mediante Django Forms.
* Tokens CSRF en todos los formularios.
* Protección de URLs mediante `get_object_or_404` para evitar errores.
* Mensajes de éxito y errores visibles al usuario.

### Interfaz de Usuario

* Diseño responsivo con Bootstrap 5.3.
* Navegación intuitiva mediante navbar.
* Plantillas con herencia (`base.html`) para evitar duplicación de código.
* Cards visuales para proyectos, assets y tareas con colores diferenciados.

## Tecnologías Utilizadas

* Python 3.12
* Django 5.2.7
* Bootstrap 5.3 (CDN)
* MySQL
* HTML5 / CSS3
* Git / GitHub

## Arquitectura del Proyecto

El proyecto sigue el patrón MVT (Model-View-Template) de Django:

* **Models** : Definición de Proyecto, DetalleProyecto, Asset, Tarea y Etiqueta.
* **Views** : Lógica para CRUD de proyectos, assets, tareas y etiquetas.
* **Templates** : Interfaces HTML dinámicas con herencia de `base.html`.
* **Forms** : Validación y procesamiento de datos.
* **Admin** : Configuración y personalización del panel de administración.

## Requisitos Previos

* Python 3.8 o superior
* pip (gestor de paquetes de Python)
* Git

## Instalación y Configuración

1. Clonar el repositorio:

<pre class="overflow-visible!" data-start="2830" data-end="2923"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2830" data-end="2923"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/Linwi-V/GameProductionManager.git
</span><span>cd</span><span> game_production
</span></span></code></div></div></pre>

2. Crear y activar entorno virtual:

**En Windows:**

<pre class="overflow-visible!" data-start="2980" data-end="3033"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2980" data-end="3033"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
venv\Scripts\activate
</span></span></code></div></div></pre>

**En Mac/Linux:**

<pre class="overflow-visible!" data-start="3055" data-end="3112"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3055" data-end="3112"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python3 -m venv venv
</span><span>source</span><span> venv/bin/activate
</span></span></code></div></div></pre>

3. Instalar dependencias:

<pre class="overflow-visible!" data-start="3142" data-end="3185"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3142" data-end="3185"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

4. Ejecutar migraciones:

<pre class="overflow-visible!" data-start="3214" data-end="3250"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3214" data-end="3250"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py migrate
</span></span></code></div></div></pre>

5. Crear superusuario para acceder al admin:

<pre class="overflow-visible!" data-start="3299" data-end="3343"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3299" data-end="3343"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py createsuperuser
</span></span></code></div></div></pre>

6. Ejecutar servidor de desarrollo:

<pre class="overflow-visible!" data-start="3383" data-end="3421"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3383" data-end="3421"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py runserver
</span></span></code></div></div></pre>

7. Acceder a la aplicación:

* Aplicación principal: `http://127.0.0.1:8000/`
* Panel de administración: `http://127.0.0.1:8000/admin/`

## Estructura del Proyecto

<pre class="overflow-visible!" data-start="3594" data-end="4648"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3594" data-end="4648"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>game_production/
├── manage.py
├── requirements.txt
├── README.md
├── game_production/           </span><span># Configuración del proyecto</span><span>
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── produccion/                </span><span># Aplicación principal</span><span>
    ├── models.py              </span><span># Modelos Proyecto, DetalleProyecto, Asset, Tarea, Etiqueta</span><span>
    ├── views.py               </span><span># Lógica de vistas CRUD</span><span>
    ├── urls.py                </span><span># URLs de la aplicación</span><span>
    ├── forms.py               </span><span># Formularios Django</span><span>
    ├── admin.py               </span><span># Configuración del panel admin</span><span>
    └── templates/
        └── produccion/
            ├── </span><span>base</span><span>.html
            ├── index.html
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
</span></span></code></div></div></pre>

## Funcionalidades Técnicas Implementadas

* Sistema de plantillas con herencia (`base.html`) y bloques dinámicos.
* Formularios Django con validación, CSRF y mensajes de error.
* CRUD completo para proyectos, assets, tareas y etiquetas.
* Panel admin personalizado.
* Integración con Bootstrap para diseño responsivo.
* Uso de relaciones 1-1, 1-N y N-M en modelos.
* Mensajes de feedback al usuario (éxito/error) usando `messages`.

## Seguridad Implementada

* Tokens CSRF en todos los formularios.
* Validación de formularios y manejo de errores.
* Uso de `get_object_or_404` para evitar errores 500.
* Control de acceso preparado para autenticación futura.

## Configuración para Producción

* `DEBUG = True` para desarrollo, debe cambiarse a `False` en producción.
* `ALLOWED_HOSTS` configurables.
* `SECRET_KEY` debe colocarse en variables de entorno para mayor seguridad.

## Aprendizajes Clave

* Arquitectura MVT de Django.
* Implementación completa de CRUD.
* Uso de Django Forms para validación.
* Integración de Bootstrap con Django.
* Manejo de relaciones FK y M2M.
* Panel admin personalizado.
* Buenas prácticas de documentación y control de versiones.

## Autor

**Linwi Vargas - Productor de Videojuegos Junior**

* GitHub: @Linwi-V
* LinkedIn: Linwi Vargas Campos
* Itch.io: linwi.itch.io

Proyecto desarrollado como parte del Bootcamp de Desarrollo Full Stack Python - Evaluación de Portafolio del Módulo 7.

## Licencia

Este proyecto es de uso educativo como parte del portafolio de aprendizaje.
