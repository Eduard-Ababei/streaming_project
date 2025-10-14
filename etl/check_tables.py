import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

print("✅ Conectado a Neon")

tables = pd.read_sql("SELECT table_name FROM information_schema.tables WHERE table_schema='public';", engine)
print("📋 Tablas disponibles:")
print(tables)

if "movies" in tables.values:
    df = pd.read_sql("SELECT * FROM movies LIMIT 10;", engine)
    print("\n🎬 Ejemplo de datos en 'movies':")
    print(df)
