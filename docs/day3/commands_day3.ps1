# Comandos PowerShell del Día 3

# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Probar conexión a Neon
python etl\check_connection_direct.py

# Aplicar esquema SQL
python etl\apply_schema_direct.py

# Comprobar tablas creadas
python etl\check_tables_direct.py

# Inicializar Git
git init
git add .
git commit -m "init: entorno Python y conexión Neon configurada"
