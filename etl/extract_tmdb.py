# etl/extract_tmdb.py
# -------------------------------------------------------
# Fase: Extracción de datos (Día 9)
# Objetivo: Conectar con la API de TMDB, descargar información de películas
# y generar un dataset procesado en formato CSV para el pipeline ETL.

import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# Definir endpoint base y parámetros
BASE_URL = "https://api.themoviedb.org/3/movie"
CATEGORIES = ["popular", "top_rated", "upcoming"]

OUTPUT_PATH = os.path.join("data", "processed", "movies_from_tmdb.csv")

def extract_tmdb_data(pages_per_category=2):
    """Extrae datos desde la API de TMDB y los guarda como CSV."""
    if not API_KEY:
        raise ValueError("Falta la clave TMDB_API_KEY en el archivo .env")

    all_movies = []

    for category in CATEGORIES:
        print(f"📡 Extrayendo categoría: {category}")
        for page in range(1, pages_per_category + 1):
            url = f"{BASE_URL}/{category}"
            params = {"api_key": API_KEY, "language": "en-US", "page": page}
            response = requests.get(url, params=params)

            if response.status_code != 200:
                print(f"⚠️  Error al obtener {category} página {page}")
                continue

            data = response.json().get("results", [])
            for movie in data:
                all_movies.append({
                    "id": movie.get("id"),
                    "title": movie.get("title"),
                    "release_date": movie.get("release_date"),
                    "original_language": movie.get("original_language"),
                    "vote_average": movie.get("vote_average"),
                    "vote_count": movie.get("vote_count"),
                    "popularity": movie.get("popularity"),
                    "category": category
                })

    # Convertir a DataFrame
    df = pd.DataFrame(all_movies)
    print(f"✅ Total de películas extraídas: {len(df)}")

    # Guardar CSV
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"💾 Datos guardados en {OUTPUT_PATH}")

    return df


if __name__ == "__main__":
    extract_tmdb_data()
