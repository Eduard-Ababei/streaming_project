import pandas as pd
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data"
csv_path = data_path / "movies_raw.csv"
output_path = data_path / "movies_clean.csv"

print("🚀 Iniciando limpieza del dataset...")
df = pd.read_csv(csv_path)
print(f"✅ Datos cargados: {len(df)} filas, {len(df.columns)} columnas")

df = df[["title", "release_year", "listed_in", "rating", "country"]].dropna()
print(f"🧹 Limpieza completa: {len(df)} filas finales")

df.to_csv(output_path, index=False)
print(f"✅ Archivo limpio guardado en: {output_path}")
