# PlaygroundFinalProject+RobertoGarcia

# Multilingo - Proyecto Final de Playground por Roberto García

Multilingo es una aplicación web de una escuela de idiomas diseñada para el Proyecto Final de Playground.

En este link puedes mirar la pagina funcionando

https://www.youtube.com/watch?v=-M7_xBS74ko

## Resumen

Multilingo es una plataforma que permite a los usuarios aprender diferentes idiomas. Admite tres idiomas principales: inglés, español y francés. Los usuarios pueden registrarse como estudiantes en estos idiomas y acceder a funciones específicas relacionadas con cada idioma.

## Características

- **Roles de usuario:**
  - **Profesores:** Usuarios especiales con privilegios extendidos, pueden crear, actualizar y administrar tareas para todos los idiomas.
  - **Estudiantes:** Usuarios registrados asociados a un idioma específico, pueden ver y gestionar sus propias tareas dentro de su idioma.

- **Idiomas:**
  - Inglés
  - Español
  - Francés

- **Funcionalidades:**
  - Los estudiantes pueden actualizar y marcar tareas como completadas para sus respectivos idiomas.
  - Los estudiantes tienen acceso limitado y solo pueden interactuar con tareas relacionadas con el idioma que eligieron.
  - Los profesores tienen acceso completo a todas las tareas de los idiomas y pueden crear, actualizar y administrarlas.

## Empezar

Para utilizar esta aplicación localmente, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone <https://github.com/RobertFuel/proyecto_final.git>
   ```

2. Configura un entorno virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Inicia el servidor de desarrollo de Django:
    ```bash
    python manage.py runserver
    ```
5. Accede a la aplicación en http://127.0.0.1:8000/

## Uso

Regístrate como estudiante para un idioma específico (inglés, español o francés) en la página principal.
Inicia sesión en la aplicación con tu nombre de usuario y contraseña registrados.
Ve al tablero de tu idioma y gestiona tus tareas.

## Colaboradores
Roberto García
https://github.com/RobertFuel

¡Siéntete libre de contribuir y mejorar este proyecto!

## Licencia
Este proyecto está bajo la Licencia MIT.
