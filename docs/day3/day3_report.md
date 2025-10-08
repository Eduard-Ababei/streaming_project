# Día 3 – Configuración del entorno Python y Neon

## Objetivo
Dejar preparado el entorno local con Python, entorno virtual y base de datos remota Neon PostgreSQL totalmente operativa.

## Pasos realizados
1. Creación del entorno virtual `.venv` y activación.
2. Instalación de librerías desde `requirements.txt`.
3. Configuración del archivo `.env` con credenciales seguras de Neon.
4. Conexión directa SSL a Neon verificada.
5. Creación del esquema SQL base (movies, genres, ratings...).
6. Inicialización del repositorio Git y primer commit local.

## Verificaciones
- `python etl\check_connection_direct.py` → conexión correcta a Neon.
- `python etl\check_tables_direct.py` → tablas detectadas correctamente.

## Evidencias
- docs/day3/connection_ok.png
- docs/day3/check_tables.png
- docs/day3/git_init.png

## Observaciones
Todo el entorno queda operativo y listo para iniciar la carga de datos reales (Día 4).
