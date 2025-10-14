import psycopg2
import os
from dotenv import load_dotenv

print("🔍 Intentando conexión directa a Neon (sin DNS)...")

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL").replace("postgresql+psycopg2://", "postgresql://")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("✅ Conectado correctamente a Neon.")
    print("Versión del servidor:", version[0])
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Error de conexión:")
    print(e)
