import psycopg2
import ssl

print("🚀 Creando esquema SQL directamente en Neon (con SSL directo)...")

# Configuración de conexión directa
conn = psycopg2.connect(
    user="neondb_owner",
    password="npg_lIsAn4uah9MT",
    host="ep-old-lake-ab7aayzq-pooler.eu-west-2.aws.neon.tech",
    port=5432,
    dbname="neondb",
    sslmode="require"
)

cur = conn.cursor()

schema_sql = """
-- Películas
CREATE TABLE IF NOT EXISTS movies (
    movie_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    original_title TEXT,
    year INT,
    runtime_minutes INT,
    budget_usd BIGINT,
    revenue_usd BIGINT
);

-- Géneros
CREATE TABLE IF NOT EXISTS genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT UNIQUE NOT NULL
);

-- Relación película-género
CREATE TABLE IF NOT EXISTS movie_genre (
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, genre_id)
);

-- Plataformas
CREATE TABLE IF NOT EXISTS platforms (
    platform_id SERIAL PRIMARY KEY,
    platform_name TEXT UNIQUE NOT NULL
);

-- Relación película-plataforma
CREATE TABLE IF NOT EXISTS movie_platform (
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    platform_id INT REFERENCES platforms(platform_id) ON DELETE CASCADE,
    available_since DATE,
    PRIMARY KEY (movie_id, platform_id)
);

-- Ratings
CREATE TABLE IF NOT EXISTS ratings (
    rating_id SERIAL PRIMARY KEY,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    user_id INT,
    rating NUMERIC(2,1) CHECK (rating BETWEEN 0 AND 10),
    rated_at TIMESTAMP DEFAULT NOW()
);
"""

cur.execute(schema_sql)
conn.commit()

print("✅ Esquema creado correctamente en Neon.")

cur.close()
conn.close()
