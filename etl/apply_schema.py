from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os, pathlib

load_dotenv()
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise RuntimeError("❌ No se encontró DATABASE_URL en .env")

engine = create_engine(db_url)

# Leer el archivo SQL
ddl_path = pathlib.Path("sql/000_schema.sql")
if not ddl_path.exists():
    raise FileNotFoundError("No se encontró sql/000_schema.sql")

ddl = ddl_path.read_text(encoding="utf-8")

# Separar statements por ';' y ejecutarlos
stmts = [s.strip() for s in ddl.split(";") if s.strip()]

with engine.begin() as conn:
    for s in stmts:
        conn.execute(text(s))

print("✅ Esquema SQL creado correctamente en Neon.")
