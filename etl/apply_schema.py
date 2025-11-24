import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

print("🛠️ Creando tablas en Neon...")

# 1. Cargar credenciales desde .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("❌ No se encontró DATABASE_URL en el archivo .env")

# 2. Crear conexión con SQLAlchemy
engine = create_engine(DATABASE_URL)

# 3. Ruta correcta al archivo DDL
ddl_path = Path(__file__).resolve().parent.parent / "sql" / "000_schema.sql"
if not ddl_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo SQL en: {ddl_path}")

ddl_content = ddl_path.read_text(encoding="utf-8")

# 4. Ejecutar cada sentencia SQL por separado
statements = [stmt.strip() for stmt in ddl_content.split(";") if stmt.strip()]

with engine.begin() as conn:
    for stmt in statements:
        conn.execute(text(stmt))
        print("✅ Sentencia ejecutada correctamente.")

print("🎉 Esquema creado con éxito en la base de datos.")
