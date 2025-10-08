from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables del archivo .env
db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise RuntimeError("❌ No se encontró DATABASE_URL en .env")

engine = create_engine(db_url, pool_pre_ping=True)

with engine.connect() as conn:
    version = conn.execute(text("SELECT version();")).scalar()
    user = conn.execute(text("SELECT current_user;")).scalar()
    db = conn.execute(text("SELECT current_database();")).scalar()

    print("✅ Conexión correcta")
    print("Versión:", version)
    print("Usuario:", user)
    print("Base de datos:", db)
