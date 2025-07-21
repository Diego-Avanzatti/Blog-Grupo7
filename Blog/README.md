# Blog de Videojuegos - Grupo 7

Este proyecto es un Blog desarrollado con Django donde se publican reseñas de videojuegos. 

# Como ejecutar el proyecto

1. Clonar el repositorio
2. Crear un entorno virtual (python -m venv entorno) en el bash
3. Activar el entorno virtual (.\entorno\Scripts\activate) "PowerShell"
4. Istalar las dependencias (pip install -r requirements.txt)

Crear base de datos local en MySQL
Cada integrante debe crear una base de datos local en MySQL con este comando: 
#CREATE DATABASE blog_g7 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Podes usar otro nombre si queres, pero asegurate de configurarlo correctamente en el archivo .env

# Variables de Entorno (env.)
Este proyecto utiliza un archivo .env para configurar datos sensibles como el acceso a la base de datos y la clave de Django 
El archivo .env no esta incluido en el repositorio por seguridad, pero se proporciona un archivo guia llamado .env.example. Para configurarlo copiar el archivo de ejemplo, edita el archivo .env con tus datos reales y listo.

# Ejecuta migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario para usar el panel admin
python manage.py createsuperuser

# Ejecuta el servidor
python manage.py runserver

# Abri el navegador en 
http://127.0.0.1:80000

Carpeta media/ (imagenes)

* Las imagenes cargadas desde el panel de administracion se guardan en la carpeta media/
* Esta carpeta si esta incluidad en el repositorio, por lo que se puede clonar y ver imagenes de ejemplo
* Las rutas estan configuradas en settings.py y urls.py

