# Semana 02 — Entorno de trabajo en Python

El entorno virtual del curso se creó desde la raíz del repositorio con `python -m venv venv`.

En PowerShell se activa con `.\venv\Scripts\Activate.ps1`.

Para desactivar el entorno virtual se utiliza el comando `deactivate`.

Las dependencias instaladas se registraron con `pip freeze > requirements.txt`.

La carpeta `venv/` está incluida en `.gitignore` y no se sube al repositorio.

Para reconstruir el entorno en otra máquina se debe crear y activar un nuevo `venv`.

Finalmente, las dependencias se instalan con `pip install -r requirements.txt`.