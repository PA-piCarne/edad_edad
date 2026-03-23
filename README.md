# Proyecto Django - Gestión de Personas

Este proyecto crea una aplicación Django conectada a **SQLite** mediante el archivo `db.sqlite3`, compatible con **DB Browser for SQLite**.

## Funcionalidades
- Lobby principal con botones de navegación.
- Formulario para registrar personas en la tabla `Persona`.
- Pantalla con todas las personas registradas.
- Pantalla con el promedio de edades.
- Pantalla con la persona de menor edad.
- Uso explícito de funciones `lambda` en las vistas para serializar, calcular promedio y detectar la menor edad.

## Ejecutar
1. Instala dependencias:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
2. Ejecuta migraciones:
   ```bash
   python3 manage.py migrate
   ```
3. Inicia el servidor:
   ```bash
   python3 manage.py runserver
   ```

## Base de datos y DB Browser
El archivo `db.sqlite3` se genera en la raíz del proyecto. Puedes abrirlo con **DB Browser for SQLite** para inspeccionar la tabla `personas_persona`.
