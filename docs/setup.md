# Comandos de configuración del entorno (Día 3)

1. Activar entorno virtual:
.\.venv\Scripts\Activate.ps1

2. Instalar dependencias:
pip install -r requirements.txt

3. Probar conexión con Neon:
python etl\check_connection_direct.py

4. Aplicar esquema SQL:
python etl\apply_schema_direct.py

5. Comprobar tablas:
python etl\check_tables_direct.py
