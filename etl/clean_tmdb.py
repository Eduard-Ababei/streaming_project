# etl/clean_csv.py
# -------------------------------------------------------
# Fase: Limpieza de datos (Día 10)
# Objetivo: Normalizar, validar y limpiar los datos extraídos
# desde TMDB antes de cargarlos en la base de datos.

import pandas as pd
import os

INPUT_PATH = os.path.join("data", "processed", "movies_from_tmdb_demo.csv")
OUTPUT_PATH = os.path.join("data", "clean", "movies_clean.csv")

def clean_data():
    print(f"🧹 Iniciando limpieza de datos desde {INPUT_PATH}")

    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"No se encontró el archivo {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH)
    print(f"Registros originales: {len(df)}")

    # Eliminar duplicados por título
    df = df.drop_duplicates(subset=["title"])

    # Eliminar filas sin fecha o sin título
    df = df.dropna(subset=["title", "release_date"])

    # Normalizar formato de fechas
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    # Eliminar registros sin fecha válida
    df = df.dropna(subset=["release_date"])

    # Añadir columnas derivadas (año de estreno)
    df["release_year"] = df["release_date"].dt.year

    # Asegurar tipos correctos
    df["vote_average"] = df["vote_average"].astype(float)
    df["vote_count"] = df["vote_count"].astype(int)

    # Resetear índice
    df = df.reset_index(drop=True)

    # Guardar dataset limpio
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"✅ Limpieza completada. Registros finales: {len(df)}")
    print(f"💾 Archivo guardado en {OUTPUT_PATH}")

    return df


if __name__ == "__main__":
    clean_data()
