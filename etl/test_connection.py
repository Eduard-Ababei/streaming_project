import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

print("🔍 Probando conexión a la base de datos...")

# 1. Cargar credenciales desde el archivo .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ No se encontró DATABASE_URL en el archivo .env")

# 2. Crear conexión con SQLAlchemy
engine = create_engine(DATABASE_URL)

# 3. Ejecutar una consulta simple para verificar conexión
try:
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version();")).scalar()
        print("✅ Conexión exitosa a la base de datos")
        print("📦 Versión del servidor:", version)
except Exception as e:
    print("❌ Error de conexión:")
    print(e)
