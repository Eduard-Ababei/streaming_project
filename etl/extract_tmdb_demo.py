# etl/extract_tmdb_demo.py
# Script demo: simula la extracción desde TMDB (NO necesita API key).
# Útil para probar el pipeline mientras esperas la activación de la cuenta TMDB.

import pandas as pd
import os

OUTPUT_PATH = os.path.join("data", "processed", "movies_from_tmdb_demo.csv")

def extract_tmdb_demo():
    # Datos simulados (pequeña muestra)
    demo_movies = [
        {"id": 1001, "title": "Demo Movie A", "release_date": "2024-01-10",
         "original_language": "en", "vote_average": 7.1, "vote_count": 1200, "popularity": 50.3, "category": "popular"},
        {"id": 1002, "title": "Demo Movie B", "release_date": "2023-06-22",
         "original_language": "es", "vote_average": 6.5, "vote_count": 450, "popularity": 22.1, "category": "top_rated"},
        {"id": 1003, "title": "Demo Movie C", "release_date": "2025-03-05",
         "original_language": "fr", "vote_average": 8.0, "vote_count": 3400, "popularity": 124.7, "category": "upcoming"},
    ]

    df = pd.DataFrame(demo_movies)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Demo extraída y guardada en {OUTPUT_PATH} — {len(df)} registros")

if __name__ == "__main__":
    extract_tmdb_demo()
