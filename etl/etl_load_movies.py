import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

print("🔗 Conexión establecida con Neon...")

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

csv_path = os.path.join(os.path.dirname(__file__), "../data/movies_clean.csv")
df = pd.read_csv(csv_path)
print(f"📥 Dataset limpio cargado: {len(df)} filas, {len(df.columns)} columnas")

with engine.begin() as conn:
    conn.execute("DROP TABLE IF EXISTS movies CASCADE")
    df.to_sql("movies", con=conn, if_exists="replace", index=False)

print("✅ Tabla 'movies' creada y datos cargados correctamente.")
