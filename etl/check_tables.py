from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

print("🔍 Comprobando tablas en la base de datos...\n")

with engine.connect() as conn:
    rows = conn.execute(text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        ORDER BY table_name;
    """)).fetchall()

    if not rows:
        print("⚠️ No hay tablas en la base de datos.")
    else:
        print("✅ Tablas encontradas:")
        for r in rows:
            print("-", r[0])
