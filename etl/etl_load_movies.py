import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pathlib import Path

print("Conexión establecida con Neon...")

# 1. Cargar credenciales
load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

# 2. Ruta correcta al CSV limpio
csv_path = Path(__file__).resolve().parent.parent / "data" / "movies_clean.csv"

df = pd.read_csv(csv_path)
print(f"Dataset limpio cargado: {len(df)} filas, {len(df.columns)} columnas")

# 3. Carga en la base de datos
with engine.begin() as conn:
    # Eliminar tabla anterior de forma compatible con SQLAlchemy 2.0
    conn.execute(text("DROP TABLE IF EXISTS movies CASCADE"))

    # Cargar datos (to_sql ya sustituye la tabla)
    df.to_sql("movies", con=conn, if_exists="replace", index=False)

print("Tabla 'movies' creada y datos cargados correctamente.")
